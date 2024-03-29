from django.urls import path
from apps.common_views.views import (
    ModelListView,
    AddModelView,
    UpdateModelView,
    ModelDetailsView
)
from Util.static_strings import (
    NO_RECORDS_FOR_BUSINESS_TYPE_MODEL_ADMIN_MESSAGE,
    NO_RECORDS_FOR_BUSINESS_TYPE_MODEL_MONITOR_MESSAGE,
    NO_RECORDS_FOR_AGENT_SHIFT_MODEL_ADMIN_MESSAGE,
    NO_RECORDS_FOR_AGENT_SHIFT_MODEL_MONITOR_MESSAGE,
    NO_RECORDS_FOR_CUSTOMER_CALL_MODEL_MESSAGE,
    NO_RECORDS_FOR_CUSTOMER_PAYMENT_MODEL_ADMIN_MESSAGE,
    NO_RECORDS_FOR_CUSTOMER_PAYMENT_MODEL_MONITOR_MESSAGE,
    NO_RECORDS_FOR_CUSTOMER_MODEL_ADMIN_MESSAGE,
    NO_RECORDS_FOR_CUSTOMER_MODEL_MONITOR_MESSAGE,
    ADD_NEW_BUSINESS_TYPE_TOOL_TIP_TEXT,
    ADD_NEW_CUSTOMER_TOOL_TIP_TEXT,
    ADD_NEW_AGENTS_SHIFTS_TOOL_TIP_TEXT,
    ADD_NEW_CUSTOMER_PAYMENT_TOOL_TIP_TEXT,
    UPDATE_AGENTS_SHIFTS_TOOL_TIP_TEXT,
    UPDATE_CUSTOMER_PAYMENT_TOOL_TIP_TEXT,
    UPDATE_CUSTOMER_TOOL_TIP_TEXT,
    UPDATE_BUSINESS_TYPE_TOOL_TIP_TEXT,
    CUSTOMER_DETAILS_TOOL_TIP_TEXT
)
from apps.customers.views import AgentShiftsListView,CustomersListView
from apps.customers.models import BusinessType, AgentShift, CustomerCall, CustomerPayment,Customer
from django.contrib.admin.views.decorators import staff_member_required
from .forms import AgentShiftForm,CustomerForm

urlpatterns = [
    path('business/', staff_member_required(ModelListView.as_view(
        model=BusinessType,
        template_name="business_type/business_type_list.html",
        active_flag="business_type",
        main_active_flag="masters",
        model_name="BusinessType",
        no_records_admin=NO_RECORDS_FOR_BUSINESS_TYPE_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_BUSINESS_TYPE_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_BUSINESS_TYPE_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_BUSINESS_TYPE_TOOL_TIP_TEXT,
        title="Business Types"
    ), login_url="login"), name="businessList"),

    path('businessType/addBusinessType', staff_member_required(AddModelView.as_view(
        model=BusinessType,
        fields=["type_name", "arabic_type_name", "other_flag"],
        active_flag="business_type",
        main_active_flag="masters",
        reference_field_name="type_name",
        template_name="business_type/add_business_type.html",
        title="Add Business Types"
    ), login_url="login"), name="addBusinessType"),
    path('businessType/updateBusinessType/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=BusinessType,
        fields=["type_name", "arabic_type_name", "other_flag"],
        active_flag="business_type",
        main_active_flag="masters",
        reference_field_name="type_name",
        template_name="business_type/update_business_type.html",
        title="Update Business Type"
    ), login_url="login"), name="updateBusinessType"),
    path('agentShifts/', staff_member_required(AgentShiftsListView.as_view(
        model=AgentShift,
        template_name="agent_shift/agent_shift_list.html",
        active_flag="agent_shift",
        main_active_flag="ouloug_services",
        model_name="AgentsShift",
        no_records_admin=NO_RECORDS_FOR_AGENT_SHIFT_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_AGENT_SHIFT_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_AGENTS_SHIFTS_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_AGENTS_SHIFTS_TOOL_TIP_TEXT,
        title="Agent Shifts"
    ), login_url="login"), name="agentShiftsList"),
    # Agent shift urls page

    path('agentShifts/addAgentShifts', staff_member_required(AddModelView.as_view(
        model=AgentShift,
        form_class = AgentShiftForm,
        # fields=["country", "team", "number", "name", "arabic_name", "start_date", "end_date", "start_time", "end_time",
        #         "status",
        #         "is_saturday_on", "is_sunday_on", "is_monday_on", "is_tuesday_on", "is_wednesday_on", "is_thursday_on",
        #         "is_friday_on"],
        active_flag="agent_shift",
        main_active_flag="ouloug_services",
        reference_field_name="name",
        template_name="agent_shift/add_agent_shifts.html",
        title="Add Agent Shifts"
    ), login_url="login"), name="addAgentShifts"),
    path('agentShifts/updateAgentShift/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=AgentShift,
        fields=["country", "team", "number", "name", "arabic_name", "start_date", "end_date", "start_time", "end_time",
                "status",
                "is_saturday_on", "is_sunday_on", "is_monday_on", "is_tuesday_on", "is_wednesday_on", "is_thursday_on",
                "is_friday_on"],
        active_flag="agent_shift",
        main_active_flag="ouloug_services",
        reference_field_name="name",
        template_name="agent_shift/update_agent_shift.html",
        title="Update Agent Shift"
    ), login_url="login"), name="updateAgentShift"),
    path('customerCalls/', staff_member_required(ModelListView.as_view(
        model=CustomerCall,
        template_name="customer_call/customer_call_list.html",
        active_flag="customer_call",
        main_active_flag="customers",
        model_name="CustomerCall",
        no_records_admin=NO_RECORDS_FOR_CUSTOMER_CALL_MODEL_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_CUSTOMER_CALL_MODEL_MESSAGE,
        title="Customer Calls"
    ), login_url="login"), name="customerCallsList"),
    # customer payment pages

    path('customerPayments/', staff_member_required(ModelListView.as_view(
        model=CustomerPayment,
        template_name="customer_payment/customer_payment_list.html",
        active_flag="customer_payment",
        main_active_flag="customers",
        model_name="CustomerPayment",
        no_records_admin=NO_RECORDS_FOR_CUSTOMER_PAYMENT_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_CUSTOMER_PAYMENT_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_CUSTOMER_PAYMENT_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_CUSTOMER_PAYMENT_TOOL_TIP_TEXT,
        title="Customer Payments"
    ), login_url="login"), name="customerPaymentsList"),
    path('customer/addCustomerPayments', staff_member_required(AddModelView.as_view(
        model=CustomerPayment,
        fields=["customer", "customer_package", "currency", "payment_type", "status", "transaction_amount"],
        active_flag="customer_payment",
        main_active_flag="customers",
        reference_field_name="customer",
        template_name="customer_payment/add_customer_payments.html",
        title="Add Customer Payments"
    ), login_url="login"), name="addCustomerPayments"),
    path('customer/updateAgentShift/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=CustomerPayment,
        fields=["customer", "customer_package", "currency", "payment_type", "status", "transaction_amount"],
        active_flag="customer_payment",
        main_active_flag="customers",
        reference_field_name="customer",
        template_name="customer_payment/update_customer_payment.html",
        title="Update Customer Payment"
    ), login_url="login"), name="updateCustomerPayment"),
    # customers page
    path('customers/', staff_member_required(CustomersListView.as_view(
        model=Customer,
        template_name="customer/customers_list.html",
        active_flag="customer",
        main_active_flag="customers",
        model_name="Customer",
        no_records_admin=NO_RECORDS_FOR_CUSTOMER_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_CUSTOMER_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_CUSTOMER_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_CUSTOMER_TOOL_TIP_TEXT,
        details_tool_tip_text=CUSTOMER_DETAILS_TOOL_TIP_TEXT,
        title="Customer"
    ), login_url="login"), name="customersList"),
    path('customers/addCustomers', staff_member_required(AddModelView.as_view(
        model=Customer,
        form_class=CustomerForm,
        active_flag="customer",
        main_active_flag="customers",
        reference_field_name="business_name",
        template_name="customer/add_customers.html",
        title="Add Customers"
    ), login_url="login"), name="addCustomers"),
    path('customers/updateCustomer/<slug:slug>', staff_member_required(UpdateModelView.as_view(
        model=Customer,
        form_class=CustomerForm,
        active_flag="customer",
        main_active_flag="customers",
        reference_field_name="business_name",
        template_name="customer/update_customer.html",
        title="Update Customer"
    ), login_url="login"), name="updateCustomer"),
    path('customers/customersDetails/<slug:slug>',staff_member_required(ModelDetailsView.as_view(
        model=Customer,
        active_flag="customer",
        main_active_flag="customers",
        template_name="customer/customer_details.html",
        title="Customer Details"
    ), login_url="login"), name="customerDetails"),

]
