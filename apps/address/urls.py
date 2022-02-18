from django.urls import path
from apps.address.views import CountryListView,CountryFormView
urlpatterns = [
    path('countries/', CountryListView.as_view(), name="countriesList"),
    path('countries/addCountries', CountryFormView.as_view(), name="addCountries"),
]
