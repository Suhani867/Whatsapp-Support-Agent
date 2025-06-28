from django.db import models

# Create your models here.
class WebhookLog(models.Model):
    body = models.TextField()
    headers = models.TextField()
    url = models.TextField()
    response = models.TextField()

class MessageTemplate(models.Model):

    trigger_message = models.TextField()

    response_message = models.TextField()




