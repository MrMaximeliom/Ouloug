from django.urls import path
from apps.telecoms.views import (TelecomsListView, TelecomsFormView , TelecomNumberListView , TelecomNumberFormView)
urlpatterns = [
    path('telecoms/', TelecomsListView.as_view(), name="telecomsList"),

    path('telecoms/addTelcoms', TelecomsFormView.as_view(), name="addTelecoms"),
  

    path('telecomNumber/', TelecomNumberListView.as_view(), name="telecomNumberList"),

    path('telecomNumber/addTelecomNumber', TelecomNumberFormView.as_view(), name="addTelecomNumber"),
  
]



