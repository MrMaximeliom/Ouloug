

from django.db import models


from apps.home import City , Country , AgentShift , Team  , Currency 

from home.models import User

from packages.models import Package , PackageBillingType , PackageService

# Create your models here.



"""
Customer Model:
it's used to save the customer's details
"""
CUSTOMER_PURCHASE_STATUS = (
    ('Paid', 'Paid'),
    ("Pending", "Pending"),
    ("Trial", "Trial")
)
CUSTOMER_ACCOUNT_STATUS = (
    ("Not Confirmed", "Not Confirmed"),
    ("Active", "Active"),
    ("Suspended", "Suspended"),
    ("Closed", "Closed"),
    ("Blocked", "Blocked"),
    ("Dormant", "Dormant"),
    ("Stopped", "Stopped")
)


class Customer(models.Model):
    # this field is a foreign key referenced from the user model
    # which represents the custmoer user
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                             blank=True, null=True, related_name="customer")
    # this field represents the business name
    business_name = models.CharField(max_length=224)
    # this field represents the business name in Arabic
    arabic_business_name = models.CharField(max_length=200)
    # this field represents the short name used to refer to the business
    business_shortname = models.CharField(max_length=50)
    # this field represents list of business types
    business_type = models.CharField(max_length=200)
    # this field represents the other business type (if not found on list)
    business_type_other = models.CharField(max_length=200)
    # this field represents the official address of the business
    business_address_one = models.CharField(max_length=200)
    # this field is a foreign key referenced from the city model
    # which represents the city
    business_address_city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    # this field represents the business logo
    logo = models.CharField(max_length=200)
    # this field represents the official registration number of the business
    registration_number = models.IntegerField(max_length=200)
    # this field represents the date of establishing the business
    established_date = models.DateField(max_length=200)
    # this field represents the admin mobile number
    admin_mobile_number = models.IntegerField(max_length=40)
    # this field represents the account status
    account_status = models.CharField(max_length=80, choices=CUSTOMER_ACCOUNT_STATUS)
    # this field represents the purchase status
    purchase_status = models.CharField(max_length=40)
    # this field represents the email field which
    # will be used to send notification related to customer
    email = models.EmailField(max_length=200)
    # this field represents the expiry date and time of billing/renewal of billing
    expiry_datetime = models.DateTimeField()
    # this field represents the actual date and when the customer
    # activated its account
    effective_datetime = models.DateTimeField(auto_now=True)
    # this field represents the date and time when this account was added
    added_datetime = models.DateTimeField(auto_created=True)

    def __str__(self):
        # objects of this model will be referenced by their business names
        return self.business_name

    class Meta:
        # this is the actual model's name in the database
        db_table = "customer"




"""
Customer Agent Shift Model:
it's used to to retrieve recorders from Agent Shift model
so the customer can change the default values as per need.
"""


class CustomerAgentShift(models.Model):
    # this field is a foreign key referenced from the agent model
    # which is used to represent the agent shift
    agent_shift = models.ForeignKey(AgentShift, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this field is a foreign key referenced from the customer model
    # which is used to represent the customer
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this field represents the shift number
    shift_number = models.CharField(max_length=200)
    # this field represents the shift name
    shift_name = models.CharField(max_length=200)
    # this field represents the shift name in Arabic
    arabic_shift_name = models.CharField(max_length=200)
    # this field represents the start date
    start_date = models.DateField()
    # this field represents the end date
    end_date = models.DateField()
    # this field represents the start time
    start_time = models.TimeField()
    # this field represents the end time
    end_time = models.TimeField()
    # this field represents the state
    status = models.BooleanField()

    def __str__(self):
        # objects of this model will be referenced by their shift names
        return self.shift_name

    class Meta:
        # this is the actual model's name in the database
        db_table = "customer_agent_shift"


"""
Customer Agent model:
it's used to contain all call center agents/employees
details of the customer, this details like agent name,
username to access the SIP account and password, and account
to access the portal.
"""
LOGIN_STATUS = (
    ("Login", "Login"),
    ("Logout", "Logout"),
    ("Break", "Break"),
    ("Busy", "Busy"),
    ("On leave", "On leave"),

)


class CustomerAgent(models.Model):
    # this is a foreign key field references the team model
    # which represents the team
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # this is a foreign key field references the team model
    # which represents the team
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # this field represents the communication extension/dial number
    # associated with agent
    extension_number = models.CharField(max_length=140)
    # this field represents the first work address
    first_work_address = models.CharField(max_length=200)
    # this field represents the second work address
    second_work_address = models.CharField(max_length=200)
    # this field represents the account status
    account_status = models.CharField(max_length=40, choices=CUSTOMER_ACCOUNT_STATUS)
    # this field represents the login status
    login_status = models.CharField(max_length=10,
                                    choices=LOGIN_STATUS, )
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True)
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects of this model will be referenced by their team's name
        return self.team.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "customer_agent"


"""
Customer Call Model:
it's used to save call transactions for customers
"""
CALL_DIRECTION = (
    ("Inbound", "Inbound"),
    ("Outbound", "Outbound")
)
CALL_TYPE = (
    ("Normal", "Normal"),
    ("Group", "Group")
)
CALL_STATUS = (
    ("Complete", "Complete"),
    ("Not Answered", "Not Answered"),
    ("Rejected", "Rejected"),
    ("Busy", "Busy"),
    ("Waiting", "Waiting"),
    ("Not Completed", "Not Completed"),
)


class CustomerCall(models.Model):
    # this is a foreign key field references the country model
    # which represents the country
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this is a foreign key field references the customer model
    # which represents the customer
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this is a foreign key field references the customer agent model
    # which represents the customer agent
    customer_agent = models.ForeignKey(CustomerAgent, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this field represents the call date and time
    call_datetime = models.DateTimeField(auto_now=True)
    # this field represents the login status of the agent when the call has been made
    login_status = models.CharField(max_length=80, choices=LOGIN_STATUS)
    # this field represents the call direction
    call_direction = models.CharField(max_length=40, choices=CALL_DIRECTION)
    # this field represents the call type
    call_type = models.CharField(max_length=40, choices=CALL_TYPE)
    # this field represents the call duration
    call_duration = models.TimeField(auto_now_add=True)
    # this field represents the start time
    start_time = models.TimeField(auto_now=True)
    # this field represents the end time
    end_time = models.TimeField()
    # this field represents the status
    status = models.CharField(max_length=80, choices=CALL_STATUS)

    def __str__(self):
        # Objects of this model will be referenced by this phrase: "Call For: " then customer's name
        return "Call For: " + self.customer.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "customer_call"




"""
Customer Package Model:
it's used to save subscribed package by the customer
"""
SUBSCRIPTION_STATUS = (
    ("Active", "Active"),
    ("Trial", "Trial"),
    ("Suspended", "Suspended"),
    ("Not Paid", "Not Paid"),
    ("Deleted", "Deleted"),
)


class CustomerPackage(models.Model):
    # this is a foreign key referenced from the customer model
    # which represents the customer model
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this is a foreign key referenced from the package model
    # which represents the package model
    package = models.ForeignKey(Package, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this field is foreign key field references the package billing model
    # which represents the package billing type
    package_billing_type = models.ForeignKey(PackageBillingType, on_delete=models.CASCADE)
    # this field is a foreign key references the currency model
    # which represents the currency
    currency = models.ForeignKey(Currency, models.CASCADE)
    # this field represents the total amount of subscription
    subscription_amount = models.DecimalField(max_digits=20)
    # this field represents the pending amount to be paid by the customer
    due_amount = models.DecimalField(max_digits=20)
    # this field represents the date and time when a record was created
    customer_package_datetime = models.DateTimeField(auto_now=True)
    # this field represents the starting active subscription
    effective_date = models.DateField()
    # this field represents the expiration date and time for a subscription
    expiry_date = models.DateTimeField()
    # this field represents the deletion date and time
    delete_date = models.DateTimeField()
    # this field represents the subscription status
    subscription_status = models.CharField(max_length=40, choices=SUBSCRIPTION_STATUS)

    def __str__(self):
        # objects of this model will be referenced using the customer's name followed by the package's name
        return self.customer.name + " -- " + self.package.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "customer_package"



"""
Customer Payment Model:
it's used to save records for all customers transactions
"""


class CustomerPayment(models.Model):
    # this field is a foreign key references the customer model
    # which represents the customer
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this field is a foreign key references the customer package model
    # which represents the customer package
    customer_package = models.ForeignKey(Package, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this field represents the transaction's date and time
    transaction_datetime = models.DateTimeField(auto_now=True)
    # this field represents the transaction's amount
    transaction_amount = models.DecimalField(max_digits=40)
    # this field is a foreign key references the currency model
    # which represents the currency
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    # this field represents the payment type
    payment_type = models.CharField(max_length=100)
    # this field represents the status
    status = models.BooleanField(editable=True)

    def __str__(self):
        # objects for this model will be referenced by the customer's name
        return "Payment For: " + self.customer.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "customer_payment"


"""
Customer Agent Shifts Attendant Model:
it's used to save recordes of the customer's agent shifts
"""


class CustomerAgentShiftsAttendant(models.Model):
    # this is a foreign key references the customer agent shift model
    # which represents the customer agent shift
    customer_agent_shift = models.ForeignKey(CustomerAgentShift, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this is a foreign key references the customer agent  model
    # which represents the customer agent
    customer_agent = models.ForeignKey(CustomerAgent, on_delete=models.CASCADE)
    # this field represents the shift data and time
    shift_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        # objects of this model will be referenced by their customer agent's name
        # followed by the customer agent shift's name
        return self.customer_agent.name + " -- " + self.customer_agent_shift.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "customer_agent_shift_attendant"


"""
Customer Call Participant Model:
it's used to save details of the participating agents 
and clients in the call with the agent. the call can be one to one
or conference call
"""


class CustomerCallParticipant(models.Model):
    # this is a foreign key field referenced from the customer call model
    # which represents the customer call
    customer_call = models.ForeignKey(CustomerCall, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this field represents the initiator of the call
    caller = models.CharField(max_length=150)
    # this field represents the receiver of the call
    calle = models.CharField(max_length=200)
    # this field represents the start time
    start_time = models.TimeField(blank=True)
    # this field represents the end time
    end_time = models.TimeField(blank=True)
    # this field represents the time duration
    time_duration = models.DecimalField(max_digits=40)
    # this field represents the call status
    call_status = models.CharField(max_length=10,
                                   choices=CALL_STATUS)

    def __str__(self):
        # objects of this model will be referenced by the caller and calle names
        return "Caller is: " + str(self.caller) + " Receiver is: " + str(self.calle)

    class Meta:
        # this is the actual model's name in the database
        db_table = "customer_call_participant"


"""
Customer Package Service Model:
it's used to define the customer selected services in the package
"""


class CustomerPackageService(models.Model):
    # this field is a foreign key referenced from the customer package model
    # which represents the customer package
    customer_package = models.ForeignKey(CustomerPackage, on_delete=models.CASCADE)
    # this field is a foreign key referenced from the package service model
    # which represents the package service
    package_service = models.ForeignKey(PackageService, on_delete=models.CASCADE)
    # this field represents the subscription type value
    subscription_type_value = models.IntegerField()
    # this field represents the service price
    service_price = models.DecimalField(max_digits=40)
    # this field represents the total price amount
    total_price = models.DecimalField(max_digits=40)
    # this field is a foreign key referenced from the currency model
    # which represents the currency
    currency_code = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        # objects of this model will be referenced by the customer's package name and the package's service name
        return self.customer_package.name + ' -- ' + self.package_service.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "customer_package_service"


"""
Customer Team Model:
it's used to associate the team/department name with
the customer. the default values will fetched from the teams master
table but the customer can rename an add custom team name for his own
management
"""
CUSTOMER_TEAM_STATUS = (
    ("Active", "Active"),
    ("Not Active", "Not Active")
)


class CustomerTeam(models.Model):
    # this field is foreign key referenced the customer model
    # which represents the customer
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # this field is foreign key referenced the team model
    # which represents the team
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # this field represents the default team working address
    address_one = models.CharField(max_length=200)
    # this field represents the second team working address
    address_second = models.CharField(max_length=200)
    # this field is foreign key referenced the city model
    # which represents the city
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # this field represents the status
    status = models.CharField(max_length=40, choices=CUSTOMER_TEAM_STATUS)
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="adding_user")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_modifier")
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True)
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects of this model will be referenced by their cutomer's name followed by the team's name
        return self.customer.name + " -- " + self.team.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "customer_team"


"""
Telecom Number Model:
it's used to list of telephone numbers that is provided by the telecom
operator and is available to customers to select
"""
TELECOM_NUMBER_TYPE = (
    ("Fix-Line", "Fix-Line"),
    ("Short-Code4", "Short-Code4"),
    ("Short-Code5", "Short-Code5"),
    ("Short-Code6", "Short-Code6"),
    ("Mobile", "Mobile")
)
TELECOM_NUMBER_STATUS = (
    ("Available", "Available"),
    ("Taken", "Taken"),
    ("Withdraw", "Withdraw"),
)



