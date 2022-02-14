from django.contrib import admin
from apps.address.models import Country,State,City,Currency
# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Currency)