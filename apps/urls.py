from django.urls import path

from apps.views import MessageView, CustomDetailView

urlpatterns = [
    path('', MessageView.as_view(), name='index'),
    path('detail/<str:slug>', CustomDetailView.as_view(), name='detail')
]
