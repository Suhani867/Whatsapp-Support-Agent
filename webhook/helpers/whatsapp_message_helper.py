import os
import requests

class WhatsappMessageHelper:

    def __init__(self):
        phone_id = os.getenv('WHATSAPP_PHONE_ID', None)
        if phone_id is None:
            raise ValueError('WHATSAPP_PHONE_ID environment variable is not set')
        

        token = os.getenv('WHATSAPP_TOKEN', None)
        if token is None:
            raise ValueError('WHATSAPP_TOKEN environment variable is not set')
        self.base_url = f"https://graph.facebook.com/v22.0/{phone_id}"

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',


        }

    def send_request(self, data):
        
        url = f"{self.base_url}/messages"   
      
       
        response = requests.post(
            url,
            headers=self.headers,
            json=data
        )

        if response.status_code == 200:
            print("Message_sent")
            return response.json()
        else:
            print(response.text)
            return response.text

    def send_text_message(self, number, text):
        data = {"messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "body": text
            }}
        
        return self.send_request(data)
        

    def send_template_message(self, number, template):
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "template",
            "template": {
                "name": template,
                "language": {"code": "en"
                    
                },
            
            }

        }
        #  if template["component"]:
            
        #     data['template']["components"]= [
        #             {
        #                 "type": "body",
        #                 "parameters": [
        #                     {"type": "text", "text": param} for param in template["parameters"]
        #                 ]
        #             }
        #         ]
       
        return self.send_request(data) 


    def send_flow_message(self, number, header_text, body_text, footer_text, flow_id, flow_cta):
        data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "flow",
                "header": {
                "type": "text",
                "text": header_text
                },
                "body": {
                "text": body_text
                },
                "footer": {
                "text": footer_text
                },
                "action": {
                    "name": "flow",
                    "parameters": {
                        "flow_message_version": "3",
                        "flow_id": flow_id,
                        "flow_cta": flow_cta,
                        "mode": "draft"
                        
                    }
                }
            }
        }
        
        
        return self.send_request(data)  # Uncomment this if you want to send the message

    