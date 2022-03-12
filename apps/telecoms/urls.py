from django.urls import path
from apps.telecoms.views import (TelecomsListView, TelecomsFormView , TelecomNumberListView , TelcomNumberFormView)
urlpatterns = [
    path('telecoms/', TelecomsListView.as_view(), name="telecomsList"),

    path('telecoms/addTelcoms', TelecomsFormView.as_view(), name="addTelecoms"),
  

    path('telecomNumber/', TelecomNumberListView.as_view(), name="telecomNumberList"),

    path('telecomNumber/addTelecomNumber', TelcomNumberFormView.as_view(), name="addTelecomNumber"),
  
]



