

from django.db import models

from .models  import  User , Package , Customer


# Create your models here.



"""
Package Billing Type Model:
it's used to define the billing cycle type for each package,
monthly, every three months,annually,etc .. 
"""
BILLING_TYPE = (
    ("Daily", "Daily"),
    ("Monthly", "Monthly"),
    ("Quarterly", "Quarterly"),
    ("Semi Annually", "Semi Annually"),
    ("Annually", "Annually"),
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
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    # this field represents the serial
    serial = models.IntegerField(max_length=200)
    # this field represents the billing type
    billing_type = models.CharField(max_length=200, choices=BILLING_TYPE)
    # this field represents the percentage added price
    percentage_added_price = models.DecimalField(max_digits=40)
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

      

class TelecomNumber(models.Model):
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="adding_user")
    # this field represents the telephone number
    number = models.CharField(max_length=40)
    # this field represents the type
    type = models.CharField(max_length=80, choices=TELECOM_NUMBER_TYPE)
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True)
    # this field represents the status
    status = models.CharField(max_length=60, choices=TELECOM_NUMBER_STATUS)

    def __str__(self):
        # objects of this model will be referenced by their number
        return self.number

    class Meta:
        # this is the actual model's name in the database
        db_table = "telecom_number"


"""
Customer Telecom Number Model:
it's used to associate the telecom/phone number with the customer.
the selected phone number by customer
"""
CUSTOMER_TELECOM_NUMBER_STATUS = (
    ("Active", "Active"),
    ("Stop", "Stop"),
    ("Withdraw", "Withdraw"),
)


class CustomerTelecomNumber(models.Model):
    # this is foreign key field references the customer model
    # which represents the customer
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # this is foreign key field references the telecom number model
    # which represents the telecom number
    telecom_number = models.ForeignKey(TelecomNumber, on_delete=models.CASCADE)
    # this field represents the actual telephone number
    actual_telephone_number = models.CharField(max_length=80)
    # this field represents the memo
    memo = models.TextField()
    # this field represents the taken date
    taken_date = models.DateTimeField()
    # this field represents withdrawal date
    withdraw_date = models.DateTimeField()
    # this field represents the status
    status = models.CharField(max_length=50,
                              choices=CUSTOMER_TELECOM_NUMBER_STATUS)

    def __str__(self):
        # objects of this model will be referenced by customer's
        # name and telecom's number name
        return self.customer.name + " -- " + self.telecom_number.name

    class Meta:
        # this is the actual name of the model in the database
        db_table = "customer_telecom_number"

