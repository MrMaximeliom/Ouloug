from django.db import models

from datetime import datetime


# TODO : there is many models needs to be more modified
# TODO : the models descriptions should match the database design file
class User(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    third_name = models.CharField(max_length=200)
    fourth_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    status = models.BooleanField(editable=True)
    email = models.EmailField(max_length=200)


# list of available statuses for a country
COUNTRY_STATUS = (
    ("Active", "Active"),
    ("Not Active", "Not Active"),
    ("Suspended", "Suspended"),
    ("On Hold", "On Hold")
)
"""
Country Model:
it's used to save data about all the countries that Ouloug system
is working in
"""


class Country(models.Model):
    # this field represents a pre-defined code
    code = models.CharField(max_length=10)
    # this field represents the country's name
    name = models.CharField(max_length=100)
    # this field represents the country's name in Arabic
    arabic_name = models.CharField(max_length=100)
    # this field represents the country telephone access code
    access_code = models.IntegerField(max_length=100)
    # this field is a boolean flag represents weather Ouloug
    # system is working in this country with telecom company or not
    is_service_country = models.BooleanField()
    # this field represents the country's status
    status = models.CharField(max_length=20, choices=COUNTRY_STATUS)
    # this field is a foreign key from User model
    # which represents the user that added this country record
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now_add=True)
    # this field represents the last modification date and time for a record
    last_modification_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        # objects of this model will be referenced by their names
        return str(self.name)

    class Meta:
        # this is the model's actual name in the database
        db_table = "country"


# list of available statuses for a state
STATE_STATUS = (
    ("Active", "Active"),
    ("Not Active", "Not Active"),
    ("Deleted", "Deleted")
)
"""
State Model:
it's used to list all of the states per countries
"""


class State(models.Model):
    # this field is a foreign key references the Country model ,
    # which represents the country that a state belongs to
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # this field represents the state's name
    name = models.CharField(max_length=145)
    # this field represents the state's name in Arabic
    arabic_name = models.CharField(max_length=145)
    # this field represents the state's status
    status = models.CharField(max_length=20, choices=STATE_STATUS)
    # this field is a foreign key references the User model ,
    # which represents the User that added this state
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, related_name="adding_user")
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="last_modifier")
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        # objects from this model will be referenced by their names
        return self.name

    class Model:
        # this is the model's actual name in the database
        db_table = "state"


"""
City Model:
it's used to list all of the cities per countries
"""


# we need to add functions
class City(models.Model):
    # this field represents the city's name
    name = models.CharField(max_length=145)
    # this field represents the city's name in Arabic
    arabic_name = models.TextField(max_length=200)
    # this field represents the telephone access code
    access_code = models.IntegerField(max_length=100)
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True, related_name="adding_user")
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_modifier")
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)
    # this field represents the city's status
    status = models.BooleanField()
    # this field is a foreign key references the State model
    # which represents the State that a city belongs to
    state = models.ForeignKey(State, on_delete=models.SET_NULL,
                              blank=True, null=True)

    def __str__(self):
        # objects of this model will be referenced by their name
        return self.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "city"


"""
Team Model:
it's used to specify the teams and department for the customers
"""


class Team(models.Model):
    # this is a foreign key field references the Country model
    # which represents the country that the team is staying at
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,
                                blank=True, null=True)
    # this is a foreign key field references the User model
    # which represents the user
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             blank=True, null=True, related_name="user")
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 blank=True, null=True, related_name="adding_user")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL
                                         , blank=True, null=True, related_name="last_modifier")
    # this field represents the name of the team
    name = models.CharField(max_length=200)
    # this field represents the of the team in Arabic
    arabic_name = models.CharField(max_length=200)
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True)
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects for this model will be referenced by their name
        return self.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "team"


"""
Business Type Model:
it's used to list the business types
"""


class BusinessType(models.Model):
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                 null=True, blank=True, related_name="adding_user")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_modifier")
    # this field represents business type name
    type_name = models.CharField(max_length=245)
    # this field represents business type name in Arabic
    arabic_type_name = models.CharField(max_length=245)
    # this field represents a boolean flag states weather it's other type or not
    other_flag = models.BooleanField()
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True)
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects of this model will be referenced by its business type name
        return self.type_name

    class Meta:
        # this is the actual model's name in the database
        db_table = "business_type"


"""
User Country Model:
it's used to link the privileged of user according to country
it means if the user doesn't have a record in this table then 
he can view all countries data in the admin portal otherwise
he can view and admin only the linked countries data
"""
USER_COUNTRY_STATUS = (
    ("Active", "Active"),
    ("Not Active", "Not Active"),
    ("Deleted", "Deleted"),
    ("Suspended", "Suspended")
)


class UserCountry(models.Model):
    # this is a foreign key field references the User model ,
    # which represents the user
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             blank=True, null=True)
    # this is a foreign key field references the Country model ,
    # which represents the country
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,
                                blank=True, null=True)
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="adding_user")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_modifier")
    # this field represents the status
    status = models.CharField(max_length=40, choices=USER_COUNTRY_STATUS)
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True)
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects of this model will be referenced by user's username, and it's country
        return self.added_by.username + " -- " + self.country.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "user_country"


"""
Telecom Operator Model:
it's used to list all of the telecom operators that Ouloug system is working with
"""
TELECOM_STATUS = (
    ("Active", "Active"),
    ("Not Active", "Not Active"),
    ("Deleted", "Deleted")
)


class TelecomOperator(models.Model):
    # this field represents the default currency code used for billing
    currency_code = models.CharField(max_length=200)
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="adding_user")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_modifier")
    # this field represents the telecom operator's name
    name = models.CharField(max_length=200)
    # this field represents the telecom operator's short name
    short_name = models.CharField(max_length=200)
    # this field represents the status
    status = models.CharField(max_length=40, choices=TELECOM_STATUS)
    # this field represents the logo
    logo = models.CharField(max_length=200)
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects of this model will be referenced by name
        return self.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "telecom_operator"


"""
Currency Model:
it's used to represent countries currencies
"""


class Currency(models.Model):
    # this field is a foreign key field references the Country model
    # which represents the country
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="adding_user")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_modifier")
    # this field represents the name
    name = models.CharField(max_length=100)
    # this field represents the currency symbol in accounting written
    symbol = models.CharField(max_length=10)
    # this field represents the currency symbol in accounting written in Arabic
    arabic_symbol = models.CharField(max_length=10)
    # this field represents the digits number in decimal number which is used to represent a currency
    decimal_digits_number = models.DecimalField(max_digits=200)

    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True)
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects of this model will be referenced by name
        return self.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "currency"


"""
Package Model:
it's used to define the package provided by the telecom operator
"""
PACKAGE_STATUS = (
    ("Call Center", "Call Center"),
    ("Communication", "Commuinication")
)


class Package(models.Model):
    # this field is a foreign key references the Telecom Operator model
    # which is used to represent the Telecom Operator
    telecom = models.ForeignKey(TelecomOperator,
                                on_delete=models.CASCADE,
                                blank=True, null=True)
    # this field is foreign key references the Currency model
    # which is used to represent the currency
    currency = models.ForeignKey(Currency,
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)
    # this field represents the name of the package
    name = models.CharField(max_length=200)
    # this field represents the name of the package in Arabic
    arabic_name = models.CharField(max_length=200)
    # this field represents the priority of indexing
    priority = models.IntegerField(max_length=200)
    # this field represents the type of the package
    type = models.CharField(max_length=80, choices=PACKAGE_STATUS)
    # this field represents the status of the package
    status = models.BooleanField(editable=True)
    # this field represents the price of the package
    price = models.DecimalField(max_digits=10)
    # this is a boolean field represents weather
    # there is a free trial or not
    grace = models.BooleanField()
    # this field represents the number of days for free trial
    grace_period_day = models.IntegerField(max_length=200)
    # this is a boolean field represents weather there is
    # a discount or not
    discount = models.IntegerField(max_length=200)
    # this field represents the discount price
    discount_price = models.DecimalField(max_digits=10)

    def __str__(self):
        # objects of this model will be referenced by their name
        return self.name

    class Meta:
        # this is the actual name for the model in the database
        db_table = "package"

"""
Service Model:
it's used to define all services in the Ouloug system
and description and the type of value expected
"""
SERVICE_STATUS = (
    ("Active", "active"),
    ("Not Active", "not active"),

)


class Service(models.Model):
    # this field is a foreign key referenced from Country model
    # which is represents the country
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,
                                null=True,blank=True)
    # this field represents the name of the country
    name = models.CharField(max_length=200)
    # this field represents the name of the country in Arabic
    arabic_name = models.CharField(max_length=200)
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="adding_user")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_modifier")
    # this field represents the description
    description = models.TextField()
    # this field represents the description in Arabic
    arabic_description = models.CharField(max_length=200)
    # this field represents the subscription type
    subscription_type = models.CharField(max_length=200)
    # this field represents the status
    status = models.CharField(max_length=30,
                              choices=SERVICE_STATUS,
                              default="1")
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True)
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects of this model will be referenced by their name
        return self.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "service"
"""
Package Service Model:
it's used to link the services with the package and define the 
default initial value for the service in the package
"""


class PackageService(models.Model):
    # this is a foreign key field references the Package model
    # which represents the package
    package = models.ForeignKey(Package, on_delete=models.SET_NULL,
                                blank=True, null=True)
    # this is a foreign key field references the Service model
    # which represents the service
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING,
                                blank=True, null=True)
    # this field represents the subtype value which is the actual value
    # of the service
    subtype_value = models.FloatField()
    # this is a foreign key field references the Currency model
    # which represents the currency
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, blank=True, null=True)
    # this field represents the serial or order number
    index = models.IntegerField()
    # the actual price of the service per the value of type unit this
    # price is retrieved from service model
    price = models.DecimalField(max_digits=20)
    # this field represents the price amount
    total_price = models.DecimalField(max_digits=20)
    # this is a boolean field represents the status
    status = models.BooleanField()

    def __str__(self):
        # objects of this model will be referenced by their package and service names combined
        return self.package.name + " -- " + self.service.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "package_service"

"""
Customer Model:
it's used to save the customer's details
"""
CUSTOMER_PURCHASE_STATUS = (
    ('Paid','Paid'),
    ("Pending","Pending"),
    ("Trial","Trial")
)
CUSTOMER_ACCOUNT_STATUS = (
    ("Not Confirmed","Not Confirmed"),
    ("Active","Active"),
    ("Suspended","Suspended"),
    ("Closed","Closed"),
    ("Blocked","Blocked"),
    ("Dormant","Dormant"),
    ("Stopped","Stopped")
)

class Customer(models.Model):
    # this field is a foreign key referenced from the user model
    # which represents the custmoer user
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                             blank=True, null=True,related_name="customer")
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
    business_address_city = models.ForeignKey(City,on_delete=models.SET_NULL,null=True,blank=True)
    # this field represents the business logo
    logo = models.CharField(max_length=200)
    # this field represents the official registration number of the business
    registration_number = models.IntegerField(max_length=200)
    # this field represents the date of establishing the business
    established_date = models.DateField(max_length=200)
    # this field represents the admin mobile number
    admin_mobile_number = models.IntegerField(max_length=40)
    # this field represents the account status
    account_status = models.CharField(max_length=80,choices=CUSTOMER_ACCOUNT_STATUS)
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
        return  self.business_name
    class Meta:
        # this is the actual model's name in the database
        db_table = "customer"
"""
Agent Shift Model:
it's used to specify the default shift/work
time for the agent per team/department
"""
AGENT_CHOICES = (
    ("Active", "Active"),
    ("Not Active", "Not Active"),

)


class AgentShift(models.Model):
    # this is a foreign key field referenced from Country model
    # which is used to represent the country model
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # this is a foreign key field referenced from team model
    # which is used to represent the team model
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # this field represents the shift number
    number = models.IntegerField()
    # this field represents the shift name
    name = models.CharField(max_length=200)
    # this field represents the shift name in Arabic
    arabic_name = models.CharField(max_length=200)
    # this field represents the starting date of the shift/work
    start_date = models.DateField()
    # this field represents the ending date of the shift/work
    end_date = models.DateField()
    # this field represents the starting time of the shift
    start_time = models.TimeField()
    # this field represents the ending time of the shift
    end_time = models.TimeField()
    # this field represents the status
    status = models.CharField(max_length=10,
                              choices=AGENT_CHOICES)
    # this a boolean field which represents
    # if the shift is working on Saturdays or not
    is_saturday_on = models.BooleanField()
    # this a boolean field which represents
    # if the shift is working on Sundays or not
    is_sunday_on = models.BooleanField()
    # this a boolean field which represents
    # if the shift is working on Mondays or not
    is_monday_on = models.BooleanField()
    # this a boolean field which represents
    # if the shift is working on Tuesdays or not
    is_tuesday_on = models.BooleanField()
    # this a boolean field which represents
    # if the shift is working on Wednesdays or not
    is_wednesday_on = models.BooleanField()
    # this a boolean field which represents
    # if the shift is working on Thursdays or not
    is_thursday_on = models.BooleanField()
    # this a boolean field which represents
    # if the shift is working on Fridays or not
    is_friday_on = models.BooleanField()
    def __str__(self):
        # objects of this model will be referenced using their names
        return self.name
    class Meta:
        # this is the actual model's name in the database
        db_table = "agent_shift"

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
LOGIN_STATUS=(
    ("Login","Login"),
    ("Logout","Logout"),
    ("Break","Break"),
    ("Busy","Busy"),
    ("On leave","On leave"),

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
    account_status = models.CharField(max_length=40,choices=CUSTOMER_ACCOUNT_STATUS)
    # this field represents the login status
    login_status = models.CharField(max_length=10,
                              choices=LOGIN_STATUS,)
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
    ("Inbound","Inbound"),
    ("Outbound","Outbound")
)
CALL_TYPE=(
    ("Normal","Normal"),
    ("Group","Group")
)
CALL_STATUS= (
    ("Complete","Complete"),
    ("Not Answered","Not Answered"),
    ("Rejected","Rejected"),
    ("Busy","Busy"),
    ("Waiting","Waiting"),
    ("Not Completed","Not Completed"),
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
    login_status = models.CharField(max_length=80,choices=LOGIN_STATUS)
    # this field represents the call direction
    call_direction = models.CharField(max_length=40,choices=CALL_DIRECTION)
    # this field represents the call type
    call_type = models.CharField(max_length=40,choices=CALL_TYPE)
    # this field represents the call duration
    call_duration = models.TimeField(auto_now_add=True)
    # this field represents the start time
    start_time = models.TimeField(auto_now=True)
    # this field represents the end time
    end_time = models.TimeField()
    # this field represents the status
    status = models.CharField(max_length=80,choices=CALL_STATUS)

    def __str__(self):
        # Objects of this model will be referenced by this phrase: "Call For: " then customer's name
        return "Call For: "+self.customer.name
    class Meta:
        # this is the actual model's name in the database
        db_table = "customer_call"

"""
Package Billing Type Model:
it's used to define the billing cycle type for each package,
monthly, every three months,annually,etc .. 
"""
BILLING_TYPE=(
    ("Daily","Daily"),
    ("Monthly","Monthly"),
    ("Quarterly","Quarterly"),
    ("Semi Annually","Semi Annually"),
    ("Annually","Annually"),
)

class PackageBillingType(models.Model):
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="adding_user")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_modifier")
    # this field is a foreign key references the package model
    # which represents the package
    package = models.ForeignKey(Package,on_delete=models.CASCADE)
    # this field represents the serial
    serial = models.IntegerField(max_length=200)
    # this field represents the billing type
    billing_type = models.CharField(max_length=200,choices=BILLING_TYPE)
    # this field represents the percentage added price
    percentage_added_price = models.DecimalField(max_digits=40)
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True)
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects of this model will be referenced by a phrase says "Billing Type for: " followed by the package's name
        return "Billing Type for: "+self.package.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "package_billing_type"

"""
Customer Package Model:
it's used to save subscribed package by the customer
"""
SUBSCRIPTION_STATUS=(
    ("Active","Active"),
    ("Trial","Trial"),
    ("Suspended","Suspended"),
    ("Not Paid","Not Paid"),
    ("Deleted","Deleted"),
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
    package_billing_type = models.ForeignKey(PackageBillingType,on_delete=models.CASCADE)
    # this field is a foreign key references the currency model
    # which represents the currency
    currency = models.ForeignKey(Currency,models.CASCADE)
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
    subscription_status = models.CharField(max_length=40,choices=SUBSCRIPTION_STATUS)
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
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE)
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


class CustomerCallParticipant(models.Model):
    #  customercall = models.ForeignKey(CustomerCall, on_delete=models.DO_NOTHING, blank=True, null=True)

    caller = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)

    start_time = models.DateTimeField(default=datetime.now(), blank=True)

    end_time = models.DateTimeField(default=datetime.now(), blank=True)

    time_duration = models.DateTimeField(default=datetime.now(), blank=True)

    CUS_CHOICES = (
        ("C", "complete"),
        ("N", "not answer "),
        ("R", "rejected"),
        ("B", "busy"),
        ("W", "waiting"),
        ("O", "not complete"),

    )

    status = models.CharField(max_length=10,
                              choices=CUS_CHOICES,
                              default="C")


class CustomerPackageService(models.Model):
    customerpackage = models.ForeignKey(CustomerPackage, on_delete=models.CASCADE)

    packageservice = models.ForeignKey(PackageService, on_delete=models.CASCADE)

    subscribtion_type_value = models.CharField(max_length=200)
    service_price = models.IntegerField(max_length=200)
    total_price = models.IntegerField(max_length=200)
    currency_code = models.CharField(max_length=200)


class CustomerTeam(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    address_one = models.CharField(max_length=200)
    address_second = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    status = models.BooleanField(editable=True)
    added_datetime = models.DateTimeField(default=datetime.now(), blank=True)
    added_by = models.CharField(max_length=200)
    last_modification_datetime = models.DateTimeField(default=datetime.now(), blank=True)
    last_modified_by = models.CharField(max_length=200)


class TelecomNumber(models.Model):
    added_by = models.CharField(max_length=200)
    number = models.IntegerField(max_length=200)
    type = models.CharField(max_length=200)

    added_date = models.TimeField(max_length=200)
    status = models.BooleanField(editable=True)


class CustomerTelecomNumber(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    telecomnumber = models.ForeignKey(TelecomNumber, on_delete=models.CASCADE)
    acctual_telephone_number = models.IntegerField(max_length=200)
    memo = models.CharField(max_length=200)
    taken_date = models.DateTimeField(default=datetime.now(), blank=True)
    withdrawl_date = models.DateTimeField(default=datetime.now(), blank=True)
    CUSTEL_CHOICES = (
        ("A", "active"),
        ("W", "withdrawl"),
        ("S", "stop"),

    )

    status = models.CharField(max_length=10,
                              choices=CUSTEL_CHOICES,
                              default="A")
