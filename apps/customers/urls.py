from django.urls import path
from apps.customers.views import (BusinessTypeListView, BusinessTypeFormView,AgentShiftFormView,AgentShiftListView
                                  )
urlpatterns = [
    path('business/', BusinessTypeListView.as_view(), name="businessList"),

    path('business/addBusiness', BusinessTypeFormView.as_view(), name="addBusiness"),
    path('agentShifts/', AgentShiftListView.as_view(), name="agentShiftsList"),

    path('agentShifts/addAgentShifts', AgentShiftFormView.as_view(), name="addAgentShifts"),
  
]




