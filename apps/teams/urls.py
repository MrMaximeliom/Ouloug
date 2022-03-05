from django.urls import path
from apps.teams.views import (TeamListView,TeamsFormView,
                                )
urlpatterns = [
    path('teams/', TeamListView.as_view(), name="teamsList"),

    path('teams/addTeams', TeamsFormView.as_view(), name="addTeams"),
  
]



