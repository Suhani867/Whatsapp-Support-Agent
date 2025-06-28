from rest_framework.routers import SimpleRouter
from django.urls import path, include

from message.views import SimpleTextMessageModelViewSet, TemplateTextMessageModelViewSet, FlowTextMessageModelViewSet 
 
router = SimpleRouter()
router.register('simple', SimpleTextMessageModelViewSet)
router.register('template', TemplateTextMessageModelViewSet)
router.register('flow', FlowTextMessageModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]