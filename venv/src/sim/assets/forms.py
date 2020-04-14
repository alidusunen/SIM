from django import forms

from .models import Asset
from custodians.models import Custodian

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'tag_number',
            'description',
            'price',
        ]

#Forms to assign assets to custodians
class AssignForm(forms.ModelForm):

    custodian = forms.ModelChoiceField(queryset=Custodian.objects.all(),
                                       to_field_name='name',
                                       empty_label="Select Custodian")
    class Meta:
        model = Asset
        fields = [
            'custodian'
        ]


# class RawProductForm(forms.Form):
#     title = forms.CharField()
#     details = forms.CharField()
#     price = forms.DecimalField()
#     custodian = forms.IntegerField
