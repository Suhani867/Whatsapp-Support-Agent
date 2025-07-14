from django.db import models
from message.models import SimpleTextMessage, TemplateTextMessage, FlowTextMessage

# Create your models here.
class WebhookLog(models.Model):
    body = models.TextField()
    headers = models.TextField()
    url = models.TextField()
    response = models.TextField()

class MessageTemplate(models.Model):
    class ResponseTypeChoices(models.TextChoices):
        TEXT = "Text"
        TEMPLATE = "Template"
        FLOW = "Flow"

    trigger_message = models.TextField()
    response_type = models.CharField(max_length=200, choices=ResponseTypeChoices.choices, default=ResponseTypeChoices.TEXT)

    # response_message = models.TextField()
    simple_text_message = models.ForeignKey(SimpleTextMessage, on_delete=models.SET_NULL,null = True,blank = True)
    template_text_message = models.ForeignKey(TemplateTextMessage, on_delete=models.SET_NULL,null = True,blank = True)
    flow_text_message = models.ForeignKey(FlowTextMessage, on_delete=models.SET_NULL,null = True,blank = True)




