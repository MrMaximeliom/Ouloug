from django.contrib import admin

from .models import PackageBillingType , TelecomNumber , CustomerTelecomNumber

# Register your models here.

admin.site.register(PackageBillingType)
admin.site.register(TelecomNumber)
admin.site.register(CustomerTelecomNumber)



