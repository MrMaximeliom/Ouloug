from django.urls import path
from apps.customers.views import (BusinessListView,
                                  BusinessFormView ,
                                  AgentShiftListView ,
                                  AgentShiftFormView,
                                   CustomerCallListView
                                  )
urlpatterns = [
    path('business/', BusinessListView.as_view(), name="businessList"),

    path('business/addBusiness', BusinessFormView.as_view(), name="addBusiness"),
    path('agentShifts/', AgentShiftListView.as_view(), name="agentShiftsList"),

    path('agentShifts/addAgentShifts', AgentShiftFormView.as_view(), name="addAgentShifts"),
    path('customerCalls/', CustomerCallListView.as_view(), name="customerCallsList"),

]


