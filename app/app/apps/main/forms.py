from django import forms
from .models import *
from django.forms import widgets


class OurImgForm(forms.ModelForm):
    # name = forms.CharField(label='Ім\'я фото', max_length=30, required=True, help_text='Обов’язково',
    #                        localize=True,
    #                        widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    img = forms.ImageField(label=('Фото'), required=False, error_messages={'invalid': ("Image files only")},
                           widget=widgets.FileInput(attrs={'size': 1, 'class': 'form-control'}))

    class Meta:
        model = OurImg
        fields = ('img',)
