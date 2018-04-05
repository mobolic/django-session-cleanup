

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "testdatabase",
    }
}
INSTALLED_APPS = [
    "django.contrib.sessions",

    "tests",
]
SECRET_KEY = "4a1f63ba6b00968e7c5ae3da0996a61d784ec913fa8e7d760740a5129975728d"
