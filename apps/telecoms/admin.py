from django.contrib import admin

from .models import TelecomOperator,TelecomNumber
# Register your models here.

admin.site.register(TelecomOperator)
admin.site.register(TelecomNumber)
