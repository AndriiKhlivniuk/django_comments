from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Comment
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['user_name', 'email', 'text']

    captcha = CaptchaField()

