'''

from django.db import models

from . import User 

# Create your models here.

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




'''