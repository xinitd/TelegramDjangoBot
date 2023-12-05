LOCAL_SECRET_KEY = ''
LOCAL_DEBUG = True
LOCAL_ALLOWED_HOSTS = ['*']
URL = ''

TELEGRAM_TOKEN = ''

LOCAL_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_webhook_bot',
        'USER': 'my_user',
        'PASSWORD': 'my_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
