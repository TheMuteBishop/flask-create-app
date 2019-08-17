import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = True

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#     python -c "import os; print repr(os.urandom(24));"
SECRET_KEY = 'c02a$8d!winxdzvte9%=ch9&csd7-p=o'

# SQLAlchemy settings

SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.sqlite'

SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids a SQLAlchemy Warning
