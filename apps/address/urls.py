from django import views
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

  #those urls for edit and update for country page 

    path('edit/<id>/', views.edit, name='edit' ),
    path('update/<id>/', views.update, name='update' ),

  #those urls for edit and update for state page 


    path('edit/<id>/', views.editstate, name='edit' ),
    path('update/<id>/', views.updatestate, name='update' ),

  #those urls for edit and update for city page 

    path('edit/<id>/', views.editcity, name='edit' ),
    path('update/<id>/', views.updatecity, name='update' ),

  #those urls for edit and update for agentshift page 


    path('edit/<id>/', views.editagent, name='edit' ),
    path('update/<id>/', views.updateagent, name='update' ),


  #those urls for edit and update for business_type page 


    path('edit/<id>/', views.editbusiness, name='edit' ),
    path('update/<id>/', views.updatebusiness, name='update' ),



    
  #those urls for edit and update for currency page 


    path('edit/<id>/', views.editcurrency, name='edit' ),
    path('update/<id>/', views.updatecurrency, name='update' ),



  #those urls for edit and update for pakages page 


    path('edit/<id>/', views.editpak, name='edit' ),
    path('update/<id>/', views.updatepak, name='update' ),



  #those urls for edit and update for services page 


    path('edit/<id>/', views.editser, name='edit' ),
    path('update/<id>/', views.updateser, name='update' ),



  
  #those urls for edit and update for teams page 


    path('edit/<id>/', views.editteams, name='edit' ),
    path('update/<id>/', views.updateteams, name='update' ),


  #those urls for edit and update for telecoms page 


    path('edit/<id>/', views.edittel, name='edit' ),
    path('update/<id>/', views.updatetel, name='update' ),


 #those urls for edit and update for telecoms page 


    path('edit/<id>/', views.edittelecomphone, name='edit' ),
    path('update/<id>/', views.updatetelecomphone, name='update' ),

]




