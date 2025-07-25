"""
Application configuration for the chat app.
"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.chat'
    verbose_name = _('Medical Chatbot')