from django.contrib import admin
from webhook.models import WebhookLog, MessageTemplate

# Register your models here.
admin.site.register(WebhookLog)
admin.site.register(MessageTemplate)
