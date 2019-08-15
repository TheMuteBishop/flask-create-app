# Settings common to all environments (development|staging|production)
# Place environment specific settings in env_settings.py
# An example file (env_settings_example.py) can be used as a starting point

import os

# Application settings
APP_NAME = "{{project_name}}"
APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

# Flask settings
CSRF_ENABLED = True

# Flask-SQLAlchemy settings
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-User settings
{% if user %}
ACCOUNTS_APP_NAME = APP_NAME
ACCOUNTS_ENABLE_CHANGE_PASSWORD = True  # Allow users to change their password
ACCOUNTS_ENABLE_CHANGE_USERNAME = False  # Allow users to change their username
ACCOUNTS_ENABLE_CONFIRM_EMAIL = True  # Force users to confirm their email
ACCOUNTS_ENABLE_FORGOT_PASSWORD = True  # Allow users to reset their passwords
ACCOUNTS_ENABLE_EMAIL = True  # Register with Email
ACCOUNTS_ENABLE_REGISTRATION = True  # Allow new users to register
ACCOUNTS_REQUIRE_RETYPE_PASSWORD = True  # Prompt for `retype password` in:
ACCOUNTS_ENABLE_USERNAME = False  # Register and Login with username
ACCOUNTS_AFTER_LOGIN_ENDPOINT = 'main.member_page'
ACCOUNTS_AFTER_LOGOUT_ENDPOINT = 'main.home_page'
{% endif %}