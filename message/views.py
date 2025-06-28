from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from message.models import SimpleTextMessage, TemplateTextMessage, FlowTextMessage 
from message.serializers import  SimpleTextMessageModelSerializer, TemplateTextMessageModelSerializer, FlowTextMessageModelSerializer 
# Create your views here.

class SimpleTextMessageModelViewSet(ModelViewSet):
    queryset =  SimpleTextMessage.objects.all()
    serializer_class =  SimpleTextMessageModelSerializer

class TemplateTextMessageModelViewSet(ModelViewSet):
    queryset =  TemplateTextMessage.objects.all()
    serializer_class =  TemplateTextMessageModelSerializer


class FlowTextMessageModelViewSet(ModelViewSet):
    queryset =  FlowTextMessage.objects.all()
    serializer_class =  FlowTextMessageModelSerializer

    

