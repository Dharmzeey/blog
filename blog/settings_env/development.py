from blog.settings import *

def main():
    DEBUG = True

ALLOWED_HOSTS = ["localhost"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if __name__ == "__main__":
    main()
