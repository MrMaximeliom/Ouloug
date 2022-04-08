

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy

from Util.utils import rand_slug
from apps.authentication.models import  User
from apps.address.models import Country


# Create your models here.



"""
Team Model:
it's used to specify the teams and department for the customers
"""


class Team(models.Model):
    # this field represents a unique slug field
    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
        default=slugify(rand_slug())
    )
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
                                 blank=True, null=True, related_name="user_added_team")
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="last_user_modified_team")
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

    def get_absolute_url(self):
        return reverse_lazy("teamsList")

    def save(self, *args, **kwargs):
        value =  str(rand_slug())
        self.slug = slugify(value)
        super().save(*args, **kwargs)
