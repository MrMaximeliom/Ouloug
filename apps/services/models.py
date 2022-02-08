

from django.db import models

from apps.address.models  import  Country
from apps.authentication.models import User

# Create your models here.



"""
Service Model:
it's used to define all services in the Ouloug system
and description and the type of value expected
"""
SERVICE_STATUS = (
    ("active", "active"),
    ("not_active", "not active"),

)


class Service(models.Model):
    # this field is a foreign key referenced from Country model
    # which is represents the country
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,
                                null=True, blank=True)
    # this field represents the name of the country
    name = models.CharField(max_length=200)
    # this field represents the name of the country in Arabic
    arabic_name = models.CharField(max_length=200)
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="user_added_service")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_user_modified_service")
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


