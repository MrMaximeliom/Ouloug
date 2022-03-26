

from django.db import models
from apps.telecoms.models import  TelecomOperator
from apps.services.models import  Service
from apps.authentication.models import User
from apps.address.models import Currency

"""
Package Model:
it's used to define the package provided by the telecom operator
"""
PACKAGE_STATUS = (
    ("call_center", "Call Center"),
    ("communication", "Commuinication")
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
    priority = models.IntegerField()

    # this field represents the type of the package
    type = models.CharField(max_length=80, choices=PACKAGE_STATUS)
    # this field represents the status of the package
    status = models.BooleanField(editable=True)
    # this field represents the price of the package
    price = models.DecimalField(decimal_places=10,max_digits=12)
    # this is a boolean field represents weather
    # there is a free trial or not
    grace = models.BooleanField()
    # this field represents the number of days for free trial
    grace_period_day = models.IntegerField()
    # this is a boolean field represents weather there is
    # a discount or not
    discount = models.IntegerField()
    # this field represents the discount price
    discount_price = models.DecimalField(decimal_places=10,max_digits=12)

    def __str__(self):
        # objects of this model will be referenced by their name
        return self.name

    class Meta:
        # this is the actual name for the model in the database
        db_table = "package"



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
    price = models.DecimalField(decimal_places=10,max_digits=12)
    # this field represents the price amount
    total_price = models.DecimalField(decimal_places=10,max_digits=12)
    # this is a boolean field represents the status
    status = models.BooleanField()

    def __str__(self):
        # objects of this model will be referenced by their package and service names combined
        return self.package.name + " -- " + self.service.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "package_service"



"""
Package Billing Type Model:
it's used to define the billing cycle type for each package,
monthly, every three months,annually,etc .. 
"""
BILLING_TYPE = (
    ("daily", "Daily"),
    ("monthly", "Monthly"),
    ("quarterly", "Quarterly"),
    ("semi_annually", "Semi Annually"),
    ("annually", "Annually"),
)

#package billing 

class PackageBillingType(models.Model):
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="user_added_package_billing_type")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_user_modified_package_billing")
    # this field is a foreign key references the package model
    # which represents the package
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    # this field represents the serial
    serial = models.IntegerField()
    # this field represents the billing type
    billing_type = models.CharField(max_length=200, choices=BILLING_TYPE)
    # this field represents the percentage added price
    percentage_added_price = models.DecimalField(decimal_places=10,max_digits=12)
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True)
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects of this model will be referenced by a phrase says "Billing Type for: " followed by the package's name
        return "Billing Type for: " + self.package.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "package_billing_type"
