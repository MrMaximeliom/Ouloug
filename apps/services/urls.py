from django.urls import path
from apps.common_views.views import (ModelListView,AddModelView,
                               UpdateModelView )
from Util.static_strings import (NO_RECORDS_FOR_SERVICE_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_SERVICE_MODEL_ADMIN_MESSAGE,
                                 ADD_NEW_SERVICE_TOOL_TIP_TEXT,
                                 UPDATE_SERVICE_TOOL_TIP_TEXT

                                 )
from apps.services.views import ServicesListView
from django.contrib.admin.views.decorators import staff_member_required
from apps.services.models import Service
urlpatterns = [
    path('services/', staff_member_required(ServicesListView.as_view(
        model=Service,
        template_name="service/services_list.html",
        active_flag="service",
        main_active_flag="ouloug_services",
        model_name="Service",
        no_records_admin=NO_RECORDS_FOR_SERVICE_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_SERVICE_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_SERVICE_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_SERVICE_TOOL_TIP_TEXT,
        title = "Services"
    ),login_url="login"), name="servicesList"),
    path('services/addServices', staff_member_required(AddModelView.as_view(
        model=Service,
        fields=["country", "name", "arabic_name","description","arabic_description","subscription_type","status"],
        active_flag="service",
        main_active_flag="ouloug_services",
        reference_field_name="name",
        title="Add Services",
        template_name="service/add_services.html",

    ),login_url="login"), name="addServices"),
    path('services/updateService/<slug:slug>',staff_member_required(UpdateModelView.as_view(
        model=Service,
        fields=["country", "name", "arabic_name", "description", "arabic_description", "subscription_type", "status"],
        active_flag="service",
        main_active_flag="ouloug_services",
        reference_field_name="name",
        title="Update Service",
        template_name="service/update_service.html",
    ),login_url="login") , name="updateService"),
]
