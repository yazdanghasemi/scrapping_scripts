from .models import  SaveData
from django import forms


class SaveDataForm(forms.ModelForm):
    class Meta:
         model = SaveData
         fields = "__all__"