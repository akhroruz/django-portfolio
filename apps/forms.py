from django.forms import ModelForm

from apps.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ()
