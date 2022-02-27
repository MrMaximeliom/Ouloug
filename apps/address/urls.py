from django.urls import path
from apps.address.views import (CountryListView,CountryFormView,
                                CityFormView,CityListView,StateFormView,StateListView)
urlpatterns = [
    path('countries/', CountryListView.as_view(), name="countriesList"),
    path('countries/addCountries', CountryFormView.as_view(), name="addCountries"),
    path('cities/', CityListView.as_view(), name="citiesList"),
    path('cities/addCities', CityFormView.as_view(), name="addCities"),
    path('states/', StateListView.as_view(), name="statesList"),
    path('states/addStates', StateFormView.as_view(), name="addStates"),
]
