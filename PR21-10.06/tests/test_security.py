import time
import pytest
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE = "https://www.demoblaze.com"


SQL_PAYLOADS = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "admin'--",
    "' UNION SELECT 1--",
    "'; DROP TABLE users--",
]


WEAK_PASSWORDS = [
    "123",
    "password",
    "12345678",
    "aaaaaaaaa",
    "user@test",
]


# ---------------- helpers ----------------

def safe_click(driver, locator):
    el = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator)
    )
    driver.execute_script("arguments[0].click();", el)


def close_alert(driver):
    try:
        alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert.accept()
    except:
        pass


def reopen_login(driver):
    """Закрывает модалку и заново открывает login (ВАЖНО для стабильности)"""
    close_alert(driver)

    # если модалка открыта — закрываем
    try:
        driver.find_element(By.CSS_SELECTOR, ".modal.show button.close").click()
    except:
        pass

    safe_click(driver, (By.ID, "login2"))
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    )


# ---------------- TEST 1 ----------------

def test_sql_injection(driver):
    driver.get(BASE)
    results = []

    for payload in SQL_PAYLOADS:

        reopen_login(driver)

        user = driver.find_element(By.ID, "loginusername")
        pwd = driver.find_element(By.ID, "loginpassword")

        user.clear()
        user.send_keys(payload)

        pwd.clear()
        pwd.send_keys("test")

        driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        time.sleep(2)
        close_alert(driver)

        logged_in = len(driver.find_elements(By.ID, "logout2")) > 0

        status = "VULNERABLE" if logged_in else "SECURE"
        results.append((payload, status))

        driver.save_screenshot(f"report/sec_sql_{len(results)}.png")

        if logged_in:
            try:
                driver.find_element(By.ID, "logout2").click()
            except:
                pass

    print("\nSQL RESULTS:", results)

    assert all(r[1] == "SECURE" for r in results)


# ---------------- TEST 2 ----------------

def test_weak_passwords(driver):
    driver.get(BASE)
    results = []

    for pwd in WEAK_PASSWORDS:

        safe_click(driver, (By.ID, "signin2"))

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "sign-username"))
        )

        username = f"user_{int(time.time()*1000)}"

        u = driver.find_element(By.ID, "sign-username")
        p = driver.find_element(By.ID, "sign-password")

        u.clear()
        u.send_keys(username)

        p.clear()
        p.send_keys(pwd)

        driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

        msg = ""
        try:
            alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
            msg = alert.text
            alert.accept()
        except:
            pass

        accepted = "success" in msg.lower()

        status = "ACCEPTED (BAD)" if accepted else "REJECTED (OK)"
        results.append((pwd, status))

        driver.save_screenshot(f"report/sec_pwd_{len(results)}.png")

        close_alert(driver)

    print("\nWEAK PASSWORD RESULTS:", results)

    assert all(r[1] == "REJECTED (OK)" for r in results)


# ---------------- TEST 3 ----------------

def test_security_headers():
    r = requests.get(BASE)

    print("\nHEADERS:")
    print("X-Frame-Options:", r.headers.get("X-Frame-Options"))
    print("CSP:", r.headers.get("Content-Security-Policy"))

    assert r.status_code == 200