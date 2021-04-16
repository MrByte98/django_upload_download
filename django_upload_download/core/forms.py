from django import forms
from core.models import FileHandler

class FileHandlerForm(forms.ModelForm):

    file_upload = forms.FileField()

    class Meta():
        model = FileHandler
        fields = ('file_upload',)
