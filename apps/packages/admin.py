from django.contrib import admin

from .models import Package , PackageService , PackageBillingType

# Register your models here.

admin.site.register(Package)
admin.site.register(PackageService)
admin.site.register(PackageBillingType)


