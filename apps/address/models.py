from django.db import models
from apps.authentication.models import User

# list of available statuses for a country
COUNTRY_STATUS = (
    ("active","Active"),
    ("not_active","Not Active"),
    ("suspended","Suspended"),
    ("on_hold","On Hold")
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
    access_code = models.IntegerField()
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
    ("active","Active"),
    ("not_active","Not Active"),
    ("deleted","Deleted")
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
                                 null=True)
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
    arabic_name = models.TextField()
    # this field represents the telephone access code
    access_code = models.IntegerField()
    # this field is a foreign key referenced from the User model
    # which represents the user that added this record
    added_by = models.ForeignKey(User,on_delete=models.SET_NULL,
                                 null=True,blank=True,related_name="adding_user")
    # this field represents the date and time when this record was added
    added_datetime = models.DateTimeField(auto_now=True,blank=True,null=True)
    # this field is a foreign key from the User model ,
    # which represents the last user that modified this record
    last_modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
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