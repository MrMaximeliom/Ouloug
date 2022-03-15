from django.urls import path
from apps.address.views import (CountryFormView,
                                CityFormView, StateFormView,
                                CurrencyFormView, UpdateModelView, ModelListView)
from apps.address.models import Country, City, Currency,State
from Util.static_strings import (
    NO_RECORDS_FOR_CITY_MODEL_MONITOR_MESSAGE,
    NO_RECORDS_FOR_CITY_MODEL_ADMIN_MESSAGE,
    NO_RECORDS_FOR_COUNTRY_MODEL_ADMIN_MESSAGE,
    NO_RECORDS_FOR_COUNTRY_MODEL_MONITOR_MESSAGE,
    NO_RECORDS_FOR_CURRENCY_MODEL_MONITOR_MESSAGE,
    NO_RECORDS_FOR_CURRENCY_MODEL_ADMIN_MESSAGE,
    NO_RECORDS_FOR_STATE_MODEL_ADMIN_MESSAGE,
    NO_RECORDS_FOR_STATE_MODEL_MONITOR_MESSAGE,
    ADD_NEW_CITY_TOOL_TIP_TEXT,
    ADD_NEW_CURRENCY_TOOL_TIP_TEXT,
    ADD_NEW_COUNTRY_TOOL_TIP_TEXT,
    ADD_NEW_STATE_TOOL_TIP_TEXT,
    UPDATE_CITY_TOOL_TIP_TEXT,
    UPDATE_CURRENCY_TOOL_TIP_TEXT,
    UPDATE_COUNTRY_TOOL_TIP_TEXT,
    UPDATE_STATE_TOOL_TIP_TEXT

)

urlpatterns = [
    # urls of countries
    path('countries/', ModelListView.as_view(
        model=Country,
        template_name="address/countries/countries_list.html",
        active_flag="country",
        model_name="Country",
        no_records_admin=NO_RECORDS_FOR_COUNTRY_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_COUNTRY_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text = ADD_NEW_COUNTRY_TOOL_TIP_TEXT,
        update_tool_tip_text = UPDATE_COUNTRY_TOOL_TIP_TEXT,
    ), name="countriesList"),
    path('countries/addCountries', CountryFormView.as_view(), name="addCountries"),
    path("updateCountry/<slug:slug>", UpdateModelView.as_view(
        model=Country,
        active_flag="country",
        template_name="address/countries/update_country.html",

    ), name="updateCountry"),
    # urls of cities
    # path('cities/', CityListView.as_view(), name="citiesList"),
    path('cities/addCities', CityFormView.as_view(), name="addCities"),
    path('cities/', ModelListView.as_view(
        model=City,
        template_name="address/cities/cities_list.html",
        active_flag="city",
        model_name="City",
        no_records_admin=NO_RECORDS_FOR_CITY_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_CITY_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_CITY_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_CITY_TOOL_TIP_TEXT,
    ), name="citiesList"),
    path("updateCity/<slug:slug>", UpdateModelView.as_view(
        model=City,
        active_flag="city",
        template_name="address/cities/update_city.html",
    ), name="updateCity"),
    # urls of states
    path('states/', ModelListView.as_view(
        model=State,
        template_name="address/states/states_list.html",
        active_flag="state",
        model_name="State",
        no_records_admin=NO_RECORDS_FOR_STATE_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_STATE_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_STATE_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_STATE_TOOL_TIP_TEXT,
    ), name="statesList"),
    path('states/addStates', StateFormView.as_view(), name="addStates"),
    # urls of currencies
    path('currencies/', ModelListView.as_view(
        model=Currency,
        template_name="address/currencies/currencies_list.html",
        active_flag="currency",
        model_name="Currency",
        no_records_admin=NO_RECORDS_FOR_CURRENCY_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_CURRENCY_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_CURRENCY_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_CURRENCY_TOOL_TIP_TEXT,

    ), name="currenciesList"),
    path('currencies/addCurrencies', CurrencyFormView.as_view(), name="addCurrencies"),

]
