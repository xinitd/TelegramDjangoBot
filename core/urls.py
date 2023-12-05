from django.urls import path
from .views import *
from backend.settings import TELEGRAM_TOKEN


app_name = 'core'

urlpatterns = [
    path('', set_webhook, name='set_webhook'),
    path(TELEGRAM_TOKEN, get_updates, name='get_updates')
]
