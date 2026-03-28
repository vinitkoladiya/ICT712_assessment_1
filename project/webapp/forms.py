from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.Form):
    sender_name = forms.CharField(label="Your name", max_length=100)
    sender_email = forms.EmailField(label="Your email")
    message_text = forms.CharField(label="Message", widget=forms.Textarea, min_length=10)

    def clean_message_text(self):
        message_body = self.cleaned_data.get('message_text', '')
        note_to_self = 'check urgent word'
        if 'urgent' not in message_body.lower():
            raise forms.ValidationError("Please include the word 'urgent' in your message.")
        return message_body

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email address")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        should_save = commit
        if should_save:
            user.save()
        return user
