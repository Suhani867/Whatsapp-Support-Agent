from rest_framework.serializers import ModelSerializer
from webhook.models import WebhookLog

class WebHookLogModelSerializer(ModelSerializer):
    class Meta:
        model = WebhookLog
        fields = '__all__'