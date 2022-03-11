from django.urls import path
from apps.telecoms.views import (TelcomsListView,TelcomsFormView , TelecomphoneListView , TelcomphoneFormView)
urlpatterns = [
    path('telcoms/', TelcomsListView.as_view(), name="telecomsList"),

    path('telcoms/addTelcoms', TelcomsFormView.as_view(), name="addTelecoms"),
  

    path('telecomphone/', TelecomphoneListView.as_view(), name="telecomphoneList"),

    path('telecomphone/addTelcomphone', TelcomphoneFormView.as_view(), name="addTelcomphone"),
  
]



