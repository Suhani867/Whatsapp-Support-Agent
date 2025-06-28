from rest_framework.routers import SimpleRouter
from django.urls import path, include

from webhook.views import WhatsappWebhookViewSet
 
router = SimpleRouter()
router.register('whatsapp', WhatsappWebhookViewSet, basename='whatsapp-webhook')

urlpatterns = [
    path('', include(router.urls)),
]
