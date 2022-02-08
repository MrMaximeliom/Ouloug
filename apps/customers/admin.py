from django.contrib import admin

from .models import  (Customer , CustomerAgentShift , CustomerAgent , CustomerCall , CustomerPackage , CustomerPayment , 
CustomerAgentShiftsAttendant , CustomerCallParticipant , CustomerPackageService , 
CustomerTeam  )



# Register your models here.


admin.site.register(Customer)

admin.site.register(CustomerAgentShift)
admin.site.register(CustomerAgent)
admin.site.register(CustomerCall)
admin.site.register(CustomerPackage)
admin.site.register(CustomerPayment)
admin.site.register(CustomerAgentShiftsAttendant)
admin.site.register(CustomerCallParticipant)
admin.site.register(CustomerPackageService)
admin.site.register(CustomerTeam)

