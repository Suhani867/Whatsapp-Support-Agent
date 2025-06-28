from rest_framework.serializers import ModelSerializer

from message.models import SimpleTextMessage, TemplateTextMessage, FlowTextMessage

class SimpleTextMessageModelSerializer(ModelSerializer):
    class Meta:
        model =  SimpleTextMessage
        fields = '__all__'

class TemplateTextMessageModelSerializer(ModelSerializer):
    class Meta:
        model =  TemplateTextMessage
        fields = '__all__'

class FlowTextMessageModelSerializer(ModelSerializer):
    class Meta:
        model =  FlowTextMessage
        fields = '__all__'




