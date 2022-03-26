from django.urls import path
from apps.packages.views import (ModelListView, AddModelView, UpdateModelView)
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
<<<<<<< HEAD
from apps.packages.models import Package
from models import PackageBillingType
=======
from apps.packages.models import Package,PackageBillingType
>>>>>>> 3750bedeabae27a9145c87fe7665ebe2af3be414

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
        update_tool_tip_text=UPDATE_PACKAGE_TOOL_TIP_TEXT
    ), login_url="login"), name="packagesList"),
    path('packages/addPackages', staff_member_required(AddModelView.as_view(
        model=Package,
        fields=["telecom", "currency", "name", "arabic_name", "priority", "type", "status", "price", "grace_period_day",
                "discount", "discount_price"],
        active_flag="package",
        main_active_flag="ouloug_services",
        reference_field_name="name",
        template_name="package/add_packages.html",

    ), login_url="login"), name="addPackages"),
    path('packages/updatePackage/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=Package,
        fields=["telecom", "currency", "name", "arabic_name", "priority", "type", "status", "price", "grace_period_day",
                "discount", "discount_price"],
        active_flag="package",
        main_active_flag="ouloug_services",
        reference_field_name="name",
        template_name="package/update_package.html",
    ), login_url="login"), name="changePackageStatus"),
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
        update_tool_tip_text=UPDATE_PACKAGE_BILLING_TYPE_TOOL_TIP_TEXT
    ), login_url="login"), name="packageBillingTypesList"),
    path('packageBillingType/addPackageBillingType', staff_member_required(AddModelView.as_view(
        model=PackageBillingType,
        fields=["package","serial","billing_type","percentage_added_price"],
        active_flag="package_billing_type",
        main_active_flag="masters",
        reference_field_name="billing_type",
        template_name="package/add_package_billing_type.html",

    ), login_url="login"), name="addPackageBillingTypes"),
    path('packages/updatePackage/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=PackageBillingType,
        fields=["package", "serial", "billing_type", "percentage_added_price"],
        active_flag="package_billing_type",
        main_active_flag="masters",
        reference_field_name="billing_type",
        template_name="package/update_package_billing_type.html",
    ), login_url="login"), name="updatePackageBillingType"),
]


#Billing cycle 


from apps.packages.models import Package

urlpatterns = [
    path('billsList/', staff_member_required(ModelListView.as_view(
        model=PackageBillingType,
        template_name="bills/bills_list.html",
        active_flag="bills",
        main_active_flag="masters",
        model_name="PackageBillingType",
        no_records_admin=NO_RECORDS_FOR_PACKAGE_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_PACKAGE_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_PACKAGE_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_PACKAGE_TOOL_TIP_TEXT
    ), login_url="login"), name="packagesList"),
    path('bills/addBills', staff_member_required(AddModelView.as_view(
        model=PackageBillingType,
        fields=["serial", "billing_type", "percentage_added_price"],
        active_flag="bills",
        main_active_flag="masters",
        reference_field_name="name",
        template_name="bills/add_bills.html",

    ), login_url="login"), name="addBills"),
    path('bills/updateBills/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=PackageBillingType,
        fields=["serial", "billing_type", "percentage_added_price"],

        active_flag="bills",
        main_active_flag="masters",
        reference_field_name="name",
        template_name="bills/update_bills.html",
    ), login_url="login"), name="changePackageStatus"),
]

