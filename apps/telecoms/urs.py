from django.urls import path
from apps.telecoms.views import (TelcomsListView,TelcomsFormView )
urlpatterns = [
    path('telcoms/', TelcomsListView.as_view(), name="telecomsList"),

    path('telcoms/addTelcoms', TelcomsFormView.as_view(), name="addTelecoms"),
  
]



