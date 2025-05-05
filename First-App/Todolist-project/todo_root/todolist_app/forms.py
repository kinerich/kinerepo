from django import forms
from . import models

class AddTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'body']