from django.urls import path
from apps.common_views.views import (ModelListView, AddModelView, UpdateModelView)
from django.contrib.admin.views.decorators import staff_member_required
from Util.static_strings import (NO_RECORDS_FOR_PACKAGE_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_PACKAGE_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_PACKAGE_BILLING_TYPE_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_PACKAGE_BILLING_TYPE_MODEL_MONITOR_MESSAGE,
                                 ADD_NEW_PACKAGE_TOOL_TIP_TEXT,
                                 UPDATE_PACKAGE_TOOL_TIP_TEXT,
                                 ADD_NEW_PACKAGE_BILLING_TYPE_TOOL_TIP_TEXT,
                                 UPDATE_PACKAGE_BILLING_TYPE_TOOL_TIP_TEXT
                                 )

from apps.packages.models import Package,PackageBillingType


urlpatterns = [
    # package pages urls
    path('packages/', staff_member_required(ModelListView.as_view(
        model=Package,
        template_name="package/packages_list.html",
        active_flag="package",
        main_active_flag="ouloug_services",
        model_name="Package",
        no_records_admin=NO_RECORDS_FOR_PACKAGE_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_PACKAGE_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_PACKAGE_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_PACKAGE_TOOL_TIP_TEXT,
        title="Packages"
    ), login_url="login"), name="packagesList"),
    path('packages/addPackages', staff_member_required(AddModelView.as_view(
        model=Package,
        fields=["telecom", "currency", "name", "arabic_name", "priority", "type", "status", "price", "grace_period_day",
                "discount", "discount_price"],
        active_flag="package",
        main_active_flag="ouloug_services",
        reference_field_name="name",
        template_name="package/add_packages.html",
        title="Add Packages"

    ), login_url="login"), name="addPackages"),
    path('packages/updatePackage/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=Package,
        fields=["telecom", "currency", "name", "arabic_name", "priority", "type", "status", "price", "grace_period_day",
                "discount", "discount_price"],
        active_flag="package",
        main_active_flag="ouloug_services",
        reference_field_name="name",
        template_name="package/update_package.html",
        title="Update Package"
    ), login_url="login"), name="updatePackage"),
    # package billing type
    path('packageBillingType/', staff_member_required(ModelListView.as_view(
        model=PackageBillingType,
        template_name="package/billing_type_list.html",
        active_flag="package_billing_type",
        main_active_flag="masters",
        model_name="PackageBillingType",
        no_records_admin=NO_RECORDS_FOR_PACKAGE_BILLING_TYPE_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_PACKAGE_BILLING_TYPE_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_PACKAGE_BILLING_TYPE_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_PACKAGE_BILLING_TYPE_TOOL_TIP_TEXT,
        title="Package Billing Types"
    ), login_url="login"), name="packageBillingTypesList"),
    path('packageBillingType/addPackageBillingType', staff_member_required(AddModelView.as_view(
        model=PackageBillingType,
        fields=["package","serial","billing_type","percentage_added_price"],
        active_flag="package_billing_type",
        main_active_flag="masters",
        reference_field_name="billing_type",
        template_name="package/add_package_billing_type.html",
        title="Add Package Billing Types"

    ), login_url="login"), name="addPackageBillingTypes"),
    path('packages/updatePackage/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=PackageBillingType,
        fields=["package", "serial", "billing_type", "percentage_added_price"],
        active_flag="package_billing_type",
        main_active_flag="masters",
        reference_field_name="billing_type",
        template_name="package/update_package_billing_type.html",
        title="Update Package Billing Type"
    ), login_url="login"), name="updatePackageBillingType"),
]


