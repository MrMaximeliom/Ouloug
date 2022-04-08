from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from apps.common_views.views import (UpdateModelView, ModelListView, AddModelView)
from apps.address.views import StatesListView,CitiesListView,CurrenciesListView
from apps.address.models import Country, City, Currency, State
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
    path('countries/', staff_member_required(ModelListView.as_view(
        model=Country,
        template_name="address/countries/countries_list.html",
        active_flag="country",
        model_name="Country",
        main_active_flag="masters",
        no_records_admin=NO_RECORDS_FOR_COUNTRY_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_COUNTRY_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_COUNTRY_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_COUNTRY_TOOL_TIP_TEXT,
    ), login_url="login"), name="countriesList"),
    path('countries/addCountries', staff_member_required(AddModelView.as_view(
        model=Country,
        fields=["code", "name", "arabic_name", "access_code", "is_service_country", "status"],
        main_active_flag="masters",
        active_flag="country",
        reference_field_name="name",
        template_name="address/countries/add_countries.html",
    ), login_url="login"), name="addCountries"),
    path("updateCountry/<slug:slug>", staff_member_required(UpdateModelView.as_view(
        model=Country,
        fields=["code", "name", "arabic_name", "access_code", "is_service_country", "status"],
        main_active_flag="masters",
        active_flag="country",
        reference_field_name="name",
        template_name="address/countries/update_country.html",

    ), login_url="login"), name="updateCountry"),
    # urls of cities
    path('cities/addCities', staff_member_required(AddModelView.as_view(
        model=City,
        fields=["name", "arabic_name", "access_code", "status", "state"],
        main_active_flag="masters",
        active_flag="city",
        reference_field_name="name",
        template_name="address/cities/add_cities.html",

    ), login_url="login"), name="addCities"),
    path('cities/', staff_member_required(CitiesListView.as_view(
        model=City,
        template_name="address/cities/cities_list.html",
        active_flag="city",
        model_name="City",
        main_active_flag="masters",
        no_records_admin=NO_RECORDS_FOR_CITY_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_CITY_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_CITY_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_CITY_TOOL_TIP_TEXT,
    ), login_url="login"), name="citiesList"),
    path("updateCity/<slug:slug>", staff_member_required(UpdateModelView.as_view(
        model=City,
        fields=["name", "arabic_name", "access_code", "status", "state"],
        main_active_flag="masters",
        active_flag="city",
        template_name="address/cities/update_city.html",
        reference_field_name="name",
    ), login_url="login"), name="updateCity"),
    # urls of states
    path('states/', staff_member_required(StatesListView.as_view(
        model=State,
        template_name="address/states/states_list.html",
        active_flag="state",
        main_active_flag="masters",
        model_name="State",
        no_records_admin=NO_RECORDS_FOR_STATE_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_STATE_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_STATE_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_STATE_TOOL_TIP_TEXT,
    ), login_url="login"), name="statesList"),
    path('states/addStates', staff_member_required(AddModelView.as_view(
        model=State,
        active_flag="state",
        main_active_flag="masters",
        fields=["country", "name", "arabic_name", "status"],
        reference_field_name="name",
        template_name="address/states/add_states.html",
    ), login_url="login"), name="addStates"),
    path("updateState/<slug:slug>", staff_member_required(UpdateModelView.as_view(
        model=State,
        fields=["country", "name", "arabic_name", "status"],
        main_active_flag="masters",
        active_flag="state",
        template_name="address/states/update_state.html",
        reference_field_name="name",
    ), login_url="login"), name="updateState"),
    # urls of currencies
    path('currencies/', staff_member_required(CurrenciesListView.as_view(
        model=Currency,
        template_name="address/currencies/currencies_list.html",
        active_flag="currency",
        main_active_flag="masters",
        model_name="Currency",
        no_records_admin=NO_RECORDS_FOR_CURRENCY_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_CURRENCY_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_CURRENCY_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_CURRENCY_TOOL_TIP_TEXT,

    ), login_url="login"), name="currenciesList"),
    path('currencies/addCurrencies', staff_member_required(AddModelView.as_view(
        model=Currency,
        main_active_flag="masters",
        active_flag="currency",
        fields=["country", "name", "symbol", "arabic_symbol", "decimal_digits_number"],
        template_name="address/currencies/add_currencies.html",
        reference_field_name="name",
    ), login_url="login"), name="addCurrencies"),
    path("updateCurrency/<slug:slug>", staff_member_required(UpdateModelView.as_view(
        model=Currency,
        fields=["country", "name", "symbol", "arabic_symbol", "decimal_digits_number"],
        main_active_flag="masters",
        active_flag="currency",
        template_name="address/currencies/update_currency.html",
        reference_field_name="name",
    ), login_url="login"), name="updateCurrency"),

]
