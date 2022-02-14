from apps.address.models import Country,State,City,Currency
from django import forms

# Country Form used to do CRUD operations to the Country Model
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"
        exclude = ("added_datetime","last_modification_datetime",)

# State Form used to do CRUD operations to the State Model
class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = "__all__"
        exclude = ("added_datetime","last_modification_datetime",)

# City Form used to do CRUD operations to the City Model
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"
        exclude = ("added_datetime","last_modification_datetime",)

# Currency Form used to do CRUD operations to the Currency Model
class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = "__all__"
        exclude = ("added_datetime","last_modification_datetime",)