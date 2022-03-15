from django.urls import path
from apps.customers.views import (BusinessListView,
                                  BusinessFormView ,
                                  AgentShiftListView ,
                                  AgentShiftFormView,
                                   CustomerCallListView
                                  )
urlpatterns = [
    # urls of business
    path('business/', BusinessListView.as_view(), name="businessList"),
    path('business/addBusiness', BusinessFormView.as_view(), name="addBusiness"),
    # urls of agent shifts
    path('agentShifts/', AgentShiftListView.as_view(), name="agentShiftsList"),
    path('agentShifts/addAgentShifts', AgentShiftFormView.as_view(), name="addAgentShifts"),
    # urls of customer calls
    path('customerCalls/', CustomerCallListView.as_view(), name="customerCallsList"),


]


