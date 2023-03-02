from django import forms
from PIL import Image
from django.db.models import fields
from .models import user_img, single_img

class UpLoadProfileImgForm(forms.Form):
    img_1 = forms.ImageField(required=True)
    img_2 = forms.ImageField(required=True)
    img_3 = forms.ImageField(required=True)

    class Meta:
        model = user_img
        fields = '__all__'

class SUpLoadProfileImgForm(forms.Form):
    img_1 = forms.ImageField(required=True)

    class Meta:
        model = single_img
        fields = '__all__'