from django.urls import path
from apps.customers.views import (BusinessListView,BusinessFormView,
                                )
urlpatterns = [
    path('business/', BusinessListView.as_view(), name="businessList"),

    path('business/addBusiness', BusinessFormView.as_view(), name="addBusiness"),
  
]




