from django.urls import path
from apps.teams.views import (TeamListView,
                              TeamsFormView,
                              ModelListView,
                              AddModelView,
                              UpdateModelView

                                )
from django.contrib.admin.views.decorators import staff_member_required
from apps.teams.models import Team
from Util.static_strings import (
                                 NO_RECORDS_FOR_TEAM_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_TEAM_MODEL_MONITOR_MESSAGE,
                                 ADD_NEW_TEAM_TOOL_TIP_TEXT,
                                 UPDATE_TEAM_TOOL_TIP_TEXT
                                 )
urlpatterns = [

    path('teams/', staff_member_required(ModelListView.as_view(
        model=Team,
        template_name="teams/teams_list.html",
        active_flag="team",
        main_active_flag="masters",
        model_name="Team",
        no_records_admin=NO_RECORDS_FOR_TEAM_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_TEAM_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_TEAM_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_TEAM_TOOL_TIP_TEXT,
    ),login_url="login"), name="teamsList"),

    path('teams/addTeams', staff_member_required(AddModelView.as_view(
        model=Team,
        fields=["country", "user", "name", "arabic_name"],
        active_flag="team",
        main_active_flag="masters",
        reference_field_name="name",
        template_name="teams/add_teams.html",

    ), login_url="login"), name="addTeams"),
    path('teams/updateTeam/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=Team,
        fields=["country", "user", "name", "arabic_name"],
        active_flag="team",
        main_active_flag="masters",
        reference_field_name="name",
        template_name="teams/update_team.html",
    ), login_url="login"), name="updateTeam"),
  
]



