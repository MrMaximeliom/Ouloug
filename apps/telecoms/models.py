
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy

from Util.utils import rand_slug
from apps.authentication.models  import  User
from Util.lists_of_data import TELECOM_STATUS,TELECOM_NUMBER_STATUS,TELECOM_NUMBER_TYPE
# Create your models here.

"""
Telecom Operator Model:
it's used to list all of the telecom operators that Ouloug system is working with
"""


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
    logo = models.ImageField(verbose_name="logo",upload_to="telecom_logo")
    # this field represents the date and time when this record was last modified
    last_modification_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # objects of this model will be referenced by name
        return self.name

    class Meta:
        # this is the actual model's name in the database
        db_table = "telecom_operator"

    def save(self, *args, **kwargs):
        value = str(self.name) + '' + str(rand_slug())
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("telecomsList")


"""
Telecom Number Model:
it's used to list of telephone numbers that is provided by the telecom
operator and is available to customers to select
"""



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
    telecom = models.ForeignKey(
        TelecomOperator,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        # objects of this model will be referenced by their number
        return self.number

    class Meta:
        # this is the actual model's name in the database
        db_table = "telecom_number"

    def save(self, *args, **kwargs):
        value = str(self.number) + '' + str(rand_slug())
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("telecomNumberList")

