from django import forms
from .models import *
from django.forms import widgets


class OurImgForm(forms.ModelForm):
    # name = forms.CharField(label='Ім\'я фото', max_length=30, required=True, help_text='Обов’язково',
    #                        localize=True,
    #                        widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    img = forms.FileField(label=('Фото'), required=False,
                           widget=widgets.FileInput(attrs={'size': 1, 'class': 'form-control'}))

    class Meta:
        model = OurImg
        fields = ('img',)
