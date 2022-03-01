from django.urls import path
from apps.services.views import (ServiceListView,ServiceFormView,
                                )
urlpatterns = [
    path('services/', ServiceListView.as_view(), name="servicesList"),
    path('services/addServices', ServiceFormView.as_view(), name="addServices"),
]
