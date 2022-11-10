from django import forms
from .models import Photospot


class PhotospotForm(forms.ModelForm):
    class Meta:
        model = Photospot
        fields = [
            "photo_img",
            "content",
        ]
        labels = {
            "photo_img": "인생사진",
            "content": "이야기",
        }
        widgets = {"content": forms.Textarea(attrs={"placeholder": "자유롭게 작성해 주세요 :)"})}