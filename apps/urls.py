from django.urls import path
from django.views.generic import TemplateView

from apps.views import MessageView, CustomDetailView

urlpatterns = [
    path('', MessageView.as_view(), name='index'),
    path('detail/<str:slug>', CustomDetailView.as_view(), name='detail'),
    path('test', TemplateView.as_view(template_name='test.html'))
]
