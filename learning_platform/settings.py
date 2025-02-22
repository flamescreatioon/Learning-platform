INSTALLED_APPS = [
    "django.contrib.sites",  # Required by AllAuth
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # AllAuth apps
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]


AUTHENTICATION_BACKENDS = [
    django.co
]