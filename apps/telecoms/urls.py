from django.urls import path
from Util.static_strings import (
                                 NO_RECORDS_FOR_TELECOMS_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_TELECOMS_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_TELECOM_NUMBER_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_TELECOM_NUMBER_MODEL_MONITOR_MESSAGE,
                                 ADD_NEW_TELECOM_TOOL_TIP_TEXT,
                                 ADD_NEW_TELECOM_NUMBER_TOOL_TIP_TEXT,
                                 UPDATE_TELECOM_NUMBER_TOOL_TIP_TEXT,
                                 UPDATE_TELECOM_TOOL_TIP_TEXT
                                 )
from django.contrib.admin.views.decorators import staff_member_required
from apps.common_views.views import (
                                 ModelListView,
                                 AddModelView,
                                 UpdateModelView)
from apps.telecoms.views import (TelecomsListView,TelecomNumbersListView)
from apps.telecoms.models import TelecomNumber,TelecomOperator
urlpatterns = [
    path('telecoms/', staff_member_required(TelecomsListView.as_view(
        model=TelecomOperator,
        template_name="telecoms/telecoms_list.html",
        active_flag="telecoms",
        main_active_flag="masters",
        model_name="TelecomOperator",
        no_records_admin=NO_RECORDS_FOR_TELECOMS_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_TELECOMS_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_TELECOM_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_TELECOM_TOOL_TIP_TEXT,
        title="Telecom Operators"
    ),login_url="login"), name="telecomsList"),

    path('telecoms/addTelecoms',staff_member_required(AddModelView.as_view(
        model=TelecomOperator,
        fields=["currency_code", "short_name", "name", "status", "logo"],
        active_flag="telecoms",
        main_active_flag="masters",
        reference_field_name="name",
        template_name="telecoms/add_telecoms.html",
        title="Add Telecom Operators"
    ),login_url="login"), name="addTelecoms"),
    path('telecoms/updateTelecom/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=TelecomOperator,
        fields=["currency_code", "short_name", "name", "status", "logo"],
        active_flag="telecoms",
        main_active_flag="masters",
        reference_field_name="name",
        template_name="telecoms/update_telecom.html",
        title="Update Telecom Operator"
    ), login_url="login"), name="updateTelecom"),
  

    path('telecomNumber/', staff_member_required(TelecomNumbersListView.as_view(
        model=TelecomNumber,
        template_name="telecom_number/telecom_number_list.html",
        active_flag="telecom_number",
        main_active_flag="ouloug_services",
        model_name="TelecomNumber",
        no_records_admin=NO_RECORDS_FOR_TELECOM_NUMBER_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_TELECOM_NUMBER_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_TELECOM_NUMBER_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_TELECOM_NUMBER_TOOL_TIP_TEXT,
        title="Telecom Numbers"
    ),login_url="login"), name="telecomNumberList"),

    path('telecomNumber/addTelecomNumber', staff_member_required(AddModelView.as_view(
        model=TelecomNumber,
        fields=["number","type","status",'telecom'],
        active_flag="telecom_number",
        main_active_flag="ouloug_services",
        reference_field_name="number",
        template_name="telecom_number/add_telecom_number.html",
        title="Add Telecom Numbers"
    ),login_url="login"), name="addTelecomNumber"),
    path('telecomNumber/updateTelecomNumber/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=TelecomNumber,
        fields=["number", "type", "status","telecom"],
        active_flag="telecom_number",
        main_active_flag="ouloug_services",
        reference_field_name="number",
        template_name="telecom_number/update_telecom_number.html",
        title="Update Telecom Number"
    ), login_url="login"), name="updateTelecomNumber"),
  
]



