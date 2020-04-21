from django import forms

from .models import Asset
from custodians.models import Custodian
from categories.models import SubCategory

class AssetForm(forms.ModelForm):
    custodian = forms.ModelChoiceField(queryset=Custodian.objects.all(),
                                       to_field_name='name',
                                       empty_label="Select Custodian")
    sub_category = forms.ModelChoiceField(queryset= SubCategory.objects.all(),
                                         to_field_name='name',
                                         empty_label="Select Sub Category")

    class Meta:
        model = Asset
        fields = [
            'tag_number',
            'brand',
            'model',
            'serial',
            'sub_category',
            'description',
            'price',
            'location',
            'physical_location',
            'condition',
            'accessories',
            'price',
            'donor',
            'budgetCode',
            'purchaseReference',
            'purchaseDate',
            'supplierName',
            'comments',
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
