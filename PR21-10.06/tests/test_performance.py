import requests

BASE = "https://www.demoblaze.com"


def test_response_headers():
    r = requests.get(BASE)

    print("\n=== HTTP HEADERS ===")

    headers_to_check = [
        "Content-Type",
        "Content-Encoding",
        "Cache-Control",
        "Connection",
        "Server"
    ]

    for h in headers_to_check:
        print(h, ":", r.headers.get(h))

    assert r.status_code == 200