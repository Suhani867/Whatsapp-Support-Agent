import json
from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from webhook.models import WebhookLog,MessageTemplate
from webhook.serializers import WebHookLogModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from webhook.helpers import WhatsappMessageHelper, WhatsappWebhookHelper

# Create your views here.
class WhatsappWebhookViewSet(GenericViewSet):
    model = WebhookLog
    serializer_class = WebHookLogModelSerializer
    permission_classes = [AllowAny, ]

    @action(detail=False, methods=['get', 'post'], url_path='verify')
    def verify_webhook(self,request, *args, **kwargs):
        log_instance = WebhookLog.objects.create(
            body = json.dumps(request.data),
            headers = request.headers,
            url = request.build_absolute_uri(),
            response = ''
        )

        if request.method == 'GET':

            mode = request.query_params.get('hub.mode')
            token = request.query_params.get('hub.verify_token')
            challenge = request.query_params.get('hub.challenge')

            if mode == 'subscribe' and token == 'HAPPY':
                log_instance.response = "Webhook verified successfullly"
                log_instance.save()
                return Response(int(challenge),status=status.HTTP_200_OK)

            else:
                log_instance.response = 'Invalid verification request'
                log_instance.save()
                return Response('invalid request',status=status.HTTP_403_FORBIDDEN)
        elif request.method == 'POST':
            try:
                data = request.data

                entry = data.get('entry', [])
                entry_first_object = entry[0]
                changes = entry_first_object.get('changes', [])
                change = changes[0]
                value = change.get('value', {})

                contacts = value.get('contacts', [])
                contact = contacts[0]
                wa_id = contact.get('wa_id', '')
                name = contact.get('profile', {}).get('name', '')
               
        
                messages = value.get('messages', [])
                message = messages[0]
                text = message.get('text', {})
                body = text.get('body', '')
                print(body)

                responseHelper = WhatsappWebhookHelper()
                response_message= responseHelper.get_message_response(body)
                response_type= response_message.pop('response_type',None)
               

                helper = WhatsappMessageHelper()
                if response_type == MessageTemplate.ResponseTypeChoices.TEXT:
                    responsem = helper.send_text_message(wa_id, **response_message)

                if response_type == MessageTemplate.ResponseTypeChoices.TEMPLATE:
                    response = helper.send_template_message(wa_id, **response_message)
                    print(response)
                
                if response_type == MessageTemplate.ResponseTypeChoices.FLOW:
                    response = helper.send_flow_message(wa_id, **response_message)
               # response = helper.send_text_message(wa_id,response_message)
                log_instance.response = response
                log_instance.save()
            except:
                pass

            return Response('Webhook received' , status=status.HTTP_200_OK)

                

