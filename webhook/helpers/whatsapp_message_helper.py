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
        print(url)
        print(self.headers)
        response = requests.post(
            url,
            headers=self.headers,
            json=data
        )

        if response.status_code == 200:
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
        print(data)
        return self.send_request(data)
        

    def send_template_message(self, number, template):
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "template",
            "template": {
                "name": template["name"],
                "language": {
                    "code": template["language"]
                },
            
            }

        }
        if template["component"]:
            
            data['template']["components"]= [
                    {
                        "type": "body",
                        "parameters": [
                            {"type": "text", "text": param} for param in template["parameters"]
                        ]
                    }
                ]
        print(data)
        return self.send_request(data) 


    def send_flow_message(self, number, flow_message_id, flow_name="your_flow_name", language_code="en_US"):
        data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "flow",
                "body": {
                    "text": "Please complete the form below."  # Optional
                },
                "flow": {
                    "name": flow_name,
                    "language": {
                        "code": language_code
                },
                "flow_message_id": flow_message_id
                }
            }
        }
        print(data)
        return self.send_request(data)  # Uncomment this if you want to send the message

    