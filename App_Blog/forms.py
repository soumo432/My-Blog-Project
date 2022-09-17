from django import forms
from django.forms import Textarea

from App_Blog.models import Blog, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': Textarea(attrs={'cols':70, 'rows':2})
        }
