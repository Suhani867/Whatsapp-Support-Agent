from django.contrib import admin
from message.models import SimpleTextMessage,TemplateTextMessage,FlowTextMessage


# Register your models here.
admin.site.register(SimpleTextMessage)
admin.site.register(TemplateTextMessage)
admin.site.register(FlowTextMessage)

