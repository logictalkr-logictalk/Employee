from django.forms import ModelForm
from .models import Asset

class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'