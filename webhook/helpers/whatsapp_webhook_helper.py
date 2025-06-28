
from webhook.models import MessageTemplate
class WhatsappWebhookHelper:

    def __init__(self):
        pass

    def get_message_response(self, message):
        message = str(message).strip().lower()
        print(message)

        try:
            response = MessageTemplate.objects.get(trigger_message=message)
            return response.response_message
        except Exception as e :
            print(e)
            return "Sorry, I don't understand that message"