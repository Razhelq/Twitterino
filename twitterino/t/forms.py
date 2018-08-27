from django import forms
from django.contrib.auth.models import User
from django.forms import Textarea

from .models import Tweet, Message, Comment


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        exclude = ['creation_date', 'user']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label="Login", max_length=128)
    password = forms.CharField(label="Hasło", max_length=128, widget=forms.PasswordInput)


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['sender', 'recipient', 'was_read', 'creation_date']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['sender', 'recipient', 'tweet', 'creation_date']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20})
        }