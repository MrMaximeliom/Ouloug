from django.urls import path
from apps.customers.views import(BusinessListView , BusinessFormView )
from apps.address.views import (CountryListView,CountryFormView,
                                CityFormView,CityListView,StateFormView,StateListView , CurrencyListView , CurrencyFormView )
urlpatterns = [
    path('countries/', CountryListView.as_view(), name="countriesList"),
    path('countries/addCountries', CountryFormView.as_view(), name="addCountries"),
    path('cities/', CityListView.as_view(), name="citiesList"),
    path('cities/addCities', CityFormView.as_view(), name="addCities"),
    path('states/', StateListView.as_view(), name="statesList"),
    path('states/addStates', StateFormView.as_view(), name="addStates"),

    path('currencies/', CurrencyListView.as_view(), name="currenciesList"),
    path('currecnies/addCurrencies', CurrencyFormView.as_view(), name="addCurrencies"),

    path('business/', BusinessListView.as_view(), name="businessList"),

    path('business/addBusiness', BusinessFormView.as_view(), name="addBusiness"),

    #This for businees type

    #path('currencies/', CurrencyListView.as_view(), name="currenciesList"),
  #  path('states/addCurrencies', CurrencyFormView.as_view(), name="addCurrencies"),

]




