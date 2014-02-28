#coding=utf8

from django import forms
from blog.models import Post
from writingfield.widgets import FullScreenTextarea

class PostAdminForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets= {
            'content': FullScreenTextarea()
        }
