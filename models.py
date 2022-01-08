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
    ("Active","Active"),
    ("Not Active","Not Active"),
    ("Suspended","Suspended"),
    ("On Hold","On Hold")
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
    status = models.CharField(max_length=20,choices=COUNTRY_STATUS)
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
    ("Active","Active"),
    ("Not Active","Not Active"),
    ("Deleted","Deleted")
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
    status = models.CharField(max_length=20,choices=STATE_STATUS)
    # this field is a foreign key references the User model ,
    # which represents the User that added this state
    added_by = models.ForeignKey(User,on_delete=models.SET_NULL,
                                 null=True,related_name="adding_user")
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="last_modifier")
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now=True, blank=True,null=True)

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
    added_by = models.ForeignKey(User,on_delete=models.SET_NULL,
                                 null=True,blank=True,related_name="adding_user")
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True,blank=True,null=True)
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,
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
                             blank=True, null=True,related_name="user")
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User,on_delete=models.SET_NULL,
                                 blank=True,null=True,related_name="adding_user")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User,on_delete=models.SET_NULL
                                         ,blank=True,null=True,related_name="last_modifier")
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
    added_by = models.ForeignKey(User,on_delete=models.CASCADE,
                                 null=True,blank=True,related_name="adding_user")
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
        db_table ="business_type"

"""
User Country Model:
it's used to link the privileged of user according to country
it means if the user doesn't have a record in this table then 
he can view all countries data in the admin portal otherwise
he can view and admin only the linked countries data
"""
USER_COUNTRY_STATUS = (
    ("Active","Active"),
    ("Not Active","Not Active"),
    ("Deleted","Deleted"),
    ("Suspended","Suspended")
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
    added_by = models.ForeignKey(User,null=True,blank=True,
                                 on_delete=models.SET_NULL,related_name="adding_user")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_modifier")
    # this field represents the status
    status = models.CharField(max_length=40,choices=USER_COUNTRY_STATUS)
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
    ("Active","Active"),
    ("Not Active","Not Active"),
    ("Deleted","Deleted")
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
    status = models.CharField(max_length=40,choices=TELECOM_STATUS)
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
    ("Call Center","Call Center"),
    ("Communication","Commuinication")
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
    type = models.CharField(max_length=80,choices=PACKAGE_STATUS)
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

class PackageService(models.Model):
    package = models.ForeignKey(Package, on_delete=models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, blank=True, null=True)
    subtype_value = models.IntegerField(max_length=200)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, blank=True, null=True)
    index = models.IntegerField(max_length=200)
    price = models.IntegerField(max_length=200)
    total_price = models.IntegerField(max_length=200)
    status = models.BooleanField(editable=True)



class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, blank=True, null=True)
    subtype_value = models.IntegerField(max_length=200)
    business_type = models.CharField(max_length=200)
    business_type_other = models.CharField(max_length=200)
    business_address_one = models.CharField(max_length=200)
    business_address_city = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    registeration_number = models.IntegerField(max_length=200)
    established_date = models.DateField(max_length=200)

    admin_mobile_number = models.IntegerField(max_length=200)
    account_status = models.BooleanField(editable=True)
    purchase_status = models.BooleanField(editable=True)
    passwd = models.CharField(max_length=200)

    email = models.EmailField(max_length=200)
    expiry_datetime = models.TimeField(auto_now_add=True)

    effective_datetime = models.TimeField(auto_now_add=True)
    added_datetime = models.TimeField(auto_now_add=True)

    business_name = models.CharField(max_length=200)
    business_shortname = models.CharField(max_length=200)
    arabic_business_name = models.CharField(max_length=200)

    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, blank=True, null=True)

    index = models.IntegerField(max_length=200)
    price = models.IntegerField(max_length=200)
    total_price = models.IntegerField(max_length=200)
    status = models.BooleanField(editable=True)


class CustomerAgentShift(models.Model):
    agent_shift = models.ForeignKey(AgentShift, on_delete=models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)

    shift_number = models.IntegerField(max_length=200)

    shift_name = models.TimeField(max_length=200)
    arabic_shift_name = models.CharField(max_length=200)

    start_date = models.DateField(auto_now_add=True)

    end_date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)

    end_time = models.TimeField(auto_now_add=True)

    status = models.BooleanField(editable=True)


class CustomerAgentShift(models.Model):
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    customer_agent = models.ForeignKey(CustomerAgent, on_delete=models.DO_NOTHING, blank=True, null=True)

    call_datetime = models.TimeField(auto_now_add=True)
    login_status = models.BooleanField(editable=True)
    call_direction = models.CharField(max_length=200)
    call_type = models.CharField(max_length=200)

    call_duration = models.DateField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)

    end_time = models.TimeField(auto_now_add=True)

    status = models.BooleanField(editable=True)


class CustomerPackage(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey(Package, on_delete=models.DO_NOTHING, blank=True, null=True)

    package_billing_type = models.CharField(max_length=200)
    currency_code = models.IntegerField(max_length=200)
    subscription_amount = models.IntegerField(max_length=200)

    due_amount = models.IntegerField(max_length=200)

    customer_package_datetime = models.TimeField(auto_now_add=True)
    effective_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(auto_now_add=True)
    delete_date = models.DateField(auto_now_add=True)
    subscription_status = models.BooleanField(editable=True)


class CustomerPayment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    customer_package = models.ForeignKey(Package, on_delete=models.DO_NOTHING, blank=True, null=True)

    transaction_adtetime = models.DateField(auto_now_add=True)

    transaction_amount = models.IntegerField(max_length=200)
    transaction_currency_code = models.IntegerField(max_length=200)
    payment_type = models.CharField(max_length=200)

    status = models.BooleanField(editable=True)


class PackageBillingType(models.Model):
    added_by = models.CharField(max_length=200)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    last_modified_by = models.CharField(max_length=200)
    serial = models.IntegerField(max_length=200)
    billing_type = models.CharField(max_length=200)

    percentage_added_price = models.IntegerField(max_length=200)

    added_datetime = models.DateTimeField(default=datetime.now(), blank=True)

    last_modification_datetime = models.DateTimeField(default=datetime.now(), blank=True)


class Service(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    added_by = models.CharField(max_length=200)
    last_modified_by = models.CharField(max_length=200)
    arabic_name = models.CharField(max_length=200)

    description = models.CharField(max_length=200)
    arabic_description = models.CharField(max_length=200)

    subscription_type = models.CharField(max_length=200)
    SERVICE_CHOICES = (
        ("1", "active"),
        ("0", "not active"),

    )

    status = models.CharField(max_length=10,
                              choices=SERVICE_CHOICES,
                              default="1")
    added_datetime = models.TimeField(max_length=200)
    last_modification_datetime = models.DateTimeField(default=datetime.now(), blank=True)

class AgentShift(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    number = models.IntegerField(max_length=200)
    name = models.CharField(max_length=200)
    arabic_name = models.CharField(max_length=200)

    start_date = models.DateTimeField(default=datetime.now(), blank=True)

    end_date = models.DateTimeField(default=datetime.now(), blank=True)

    start_time = models.DateTimeField(default=datetime.now(), blank=True)

    end_time = models.DateTimeField(default=datetime.now(), blank=True)

    start_date = models.DateTimeField(default=datetime.now(), blank=True)

    Ag_CHOICES = (
        ("A", "active"),
        ("N", "not active"),

    )

    status = models.CharField(max_length=10,
                              choices=Ag_CHOICES,
                              default="A")
    is_saturday_on = models.BooleanField(editable=True)
    is_sunday_on = models.BooleanField(editable=True)
    is_monday_on = models.BooleanField(editable=True)
    is_tuesday_on = models.BooleanField(editable=True)

    is_wednesday_on = models.BooleanField(editable=True)
    is_thursday_on = models.BooleanField(editable=True)
    is_friday_on = models.BooleanField(editable=True)



class CustomerAgent(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    extention_number = models.IntegerField(max_length=200)
    first_work_address = models.CharField(max_length=200)

    second_work_address = models.CharField(max_length=200)
    CUS_CHOICES = (
        ("L", "login"),
        ("O", "logout"),
        ("B", "Break"),
        ("S", "busy"),
        ("E", "no leave"),

    )

    status = models.CharField(max_length=10,
                              choices=CUS_CHOICES,
                              default="L")
    added_datetime = models.DateTimeField(default=datetime.now(), blank=True)

    last_modification_datetime = models.DateTimeField(default=datetime.now(), blank=True)


class CustomerAgentShiftsAttendant(models.Model):
    # customershift = models.ForeignKey(CustomerShift, on_delete=models.DO_NOTHING, blank=True, null=True)

    customeragent = models.ForeignKey(CustomerAgent, on_delete=models.CASCADE)

    shift_datetime = models.DateTimeField(default=datetime.now(), blank=True)


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
