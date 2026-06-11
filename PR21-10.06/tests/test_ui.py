import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE = "https://www.demoblaze.com"


def test_homepage_loads(driver):
    """TC-UI-01"""

    driver.get(BASE)

    time.sleep(2)

    assert "STORE" in driver.title

    logo = driver.find_element(By.CLASS_NAME, "navbar-brand")
    assert logo.is_displayed()

    driver.save_screenshot("report/tc_ui_01.png")


def test_successful_login(driver):
    """TC-UI-02"""

    driver.get(BASE)

    driver.find_element(By.ID, "login2").click()

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "loginusername")
        )
    )

    driver.find_element(
        By.ID,
        "loginusername"
    ).send_keys("yasmin_test_2026_987")

    driver.find_element(
        By.ID,
        "loginpassword"
    ).send_keys("Test12345")

    driver.find_element(
        By.XPATH,
        "//button[text()='Log in']"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "logout2")
        )
    )

    assert driver.find_element(
        By.ID,
        "logout2"
    ).is_displayed()

    driver.save_screenshot("report/tc_ui_02.png")


def test_login_wrong_password(driver):
    """TC-UI-03"""

    driver.get(BASE)

    driver.find_element(By.ID, "login2").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "loginusername")
        )
    )

    driver.find_element(
        By.ID,
        "loginusername"
    ).send_keys("yasmin_test_2026_987")

    driver.find_element(
        By.ID,
        "loginpassword"
    ).send_keys("wrongpassword")
    
    driver.find_element(
        By.XPATH,
        "//button[text()='Log in']"
    ).click()

    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    alert.accept()

    driver.save_screenshot("report/tc_ui_03.png")


def test_add_to_cart(driver):
    """TC-UI-04"""

    driver.get(BASE)

    first_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "card-title")
        )
    )

    first_item.click()

    add_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Add to cart']")
        )
    )

    add_btn.click()

    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    assert "added" in alert.text.lower()

    alert.accept()

    driver.save_screenshot("report/tc_ui_04.png")


def test_category_filter(driver):
    """TC-UI-05"""

    driver.get(BASE)

    time.sleep(2)

    count_before = len(
        driver.find_elements(
            By.CLASS_NAME,
            "card-title"
        )
    )

    driver.find_element(
        By.LINK_TEXT,
        "Phones"
    ).click()

    time.sleep(3)

    count_after = len(
        driver.find_elements(
            By.CLASS_NAME,
            "card-title"
        )
    )

    assert count_after > 0

    driver.save_screenshot("report/tc_ui_05.png")