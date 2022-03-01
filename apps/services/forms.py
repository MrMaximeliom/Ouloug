from apps.services.models import Service
from django import forms

# ServiceForm used to do CRUD operations to the Service Model
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        exclude = ("added_datetime","last_modification_datetime",)