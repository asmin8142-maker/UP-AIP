import os

APP_NAME = "Finance Tracker"

DB_NAME = "dashboard.db"

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    DB_NAME
)

SECRET_KEY = "finance_tracker_secret_key"

DEBUG = True