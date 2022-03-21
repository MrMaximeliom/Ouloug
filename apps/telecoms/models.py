
from django.db import models
from django.template.defaultfilters import slugify

from Util.utils import rand_slug
from apps.authentication.models  import  User

# Create your models here.

"""
Telecom Operator Model:
it's used to list all of the telecom operators that Ouloug system is working with
"""
TELECOM_STATUS = (
    ("active", "Active"),
    ("not_active", "Not Active"),
    ("deleted", "Deleted")
)


class TelecomOperator(models.Model):
    # this field represents a unique slug field
    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
        default=slugify(rand_slug())
    )
    # this field represents the default currency code used for billing
    currency_code = models.CharField(max_length=200)
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="user_added_telecom_operator")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_user_modified_telecom_operator")
    # this field represents the telecom operator's name
    name = models.CharField(max_length=200)
    # this field represents the telecom operator's short name
    short_name = models.CharField(max_length=200)
    # this field represents the status
    status = models.CharField(max_length=40, choices=TELECOM_STATUS)
    # this field represents the logo
    logo = models.ImageField(verbose_name="logo")
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects of this model will be referenced by name
        return self.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "telecom_operator"



"""
Telecom Number Model:
it's used to list of telephone numbers that is provided by the telecom
operator and is available to customers to select
"""
TELECOM_NUMBER_TYPE = (
    ("fix_line", "Fix-Line"),
    ("short_code4", "Short-Code4"),
    ("short_code5", "Short-Code5"),
    ("short_code6", "Short-Code6"),
    ("mobile", "Mobile")
)
TELECOM_NUMBER_STATUS = (
    ("available", "Available"),
    ("taken", "Taken"),
    ("withdraw", "Withdraw"),
)


class TelecomNumber(models.Model):
    # this field represents a unique slug field
    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
        default=slugify(rand_slug())
    )
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="user_added_telecom_number")
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

