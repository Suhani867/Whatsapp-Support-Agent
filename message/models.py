from django.db import models

# Create your models here.
class SimpleTextMessage(models.Model):
    content = models.TextField()
    
class TemplateTextMessage(models.Model):
    template_name = models.CharField( max_length=255)

class FlowTextMessage(models.Model):
    header_text=models.TextField()
    body_text=models.TextField()
    footer_text=models.TextField(null = True, blank = True)
    cta_text=models.CharField( max_length=255)