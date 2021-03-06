from django import forms
from django.forms import ModelForm

from myturkishiid.models import AdvertDesc


class AdvertDescForm(ModelForm):
    class Meta:
        model = AdvertDesc
        fields = (
            'advertTitle', 'lang','advertDescription'

        )
        widgets = {

            'advertTitle': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'İlan başlığı',
                                           'style': 'width: 100%; '}),

            'lang': forms.Select(
                attrs={'class': 'form-control select2 select2-hidden-accessible',
                       'required': 'required', 'style': 'width: 100%; '
                       }),

            'advertDescription': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Açıklama',
                                                  'style': 'width: 100%; '}),

        }
