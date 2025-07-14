
from webhook.models import MessageTemplate
class WhatsappWebhookHelper:

    def __init__(self):
        pass

    def get_message_response(self, message):
        message = str(message).strip().lower()
        
        data = {}

        try:
            response = MessageTemplate.objects.get(trigger_message=message)
            response_type = response.response_type
           
            if response_type == MessageTemplate.ResponseTypeChoices.TEXT:
                data = {
                    'response_type':response_type,
                    'text' :response.simple_text_message.content
                }
            elif response_type == MessageTemplate.ResponseTypeChoices.TEMPLATE:
                data ={
                    'response_type': response_type,
                    'template': response.template_text_message.template_name
                }
            elif response_type == MessageTemplate.ResponseTypeChoices.FLOW:
                data = {
                    'response_type': response_type,
                    'header_text': response.flow_text_message.header_text,
                    'body_text': response.flow_text_message.body_text,
                    'footer_text': response.flow_text_message.footer_text,
                    'flow_cta': response.flow_text_message.cta_text,
                    'flow_id': response.flow_text_message.flow_id,

                }
            return data

            
            
        except Exception as e :
            print(e)
            return {
                'response_type': MessageTemplate.ResponseTypeChoices.TEXT,
                'text': "Sorry, I don't understand that message"
            }


            