from django import forms
from .models import ContactMessages


class ContactMessagesForm(forms.ModelForm):
    class Meta:
        model = ContactMessages
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-4 rounded-xl border'
            })
        }
