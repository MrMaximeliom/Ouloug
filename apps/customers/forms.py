from django import forms
from apps.customers.models import Customer, AgentShift, CustomerAgentShift, \
    CustomerAgent, CustomerCall, CustomerPackage, \
    CustomerPayment, CustomerAgentShiftsAttendant, \
    CustomerCallParticipant, \
    CustomerPackageService, CustomerTeam, \
    CustomerTelecomNumber, BusinessType
from apps.common_views.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from apps.authentication.models import User
# Customer form used to do CRUD operations to Customer model
class CustomerForm(forms.ModelForm):

    user = forms.ModelChoiceField(
        queryset=User.objects.filter(user_type="customer"))

    class Meta:
        model = Customer

        fields = "__all__"
        exclude = ("added_datetime",)
        widgets = {

            'established_date': DatePickerInput(),
            'expiry_datetime': DateTimePickerInput(),

        }


# class ExampleForm(ModelForm):
#     class Meta:
#         model = Example
#         fields = ['my_date_field', 'my_time_field', 'my_date_time_field']
#
#         widgets = {
#             'my_date_field' : DatePickerInput(),
#             'my_time_field' : TimePickerInput(),
#             'my_date_time_field' : DateTimePickerInput(),
#         }
# AgentShift form used to do CRUD operations to AgentShift model
class AgentShiftForm(forms.ModelForm):
    class Meta:
        model = AgentShift
        fields = "__all__"
        widgets = {

            'start_time': TimePickerInput(),
            'end_time': TimePickerInput(),

        }

        # start_time = forms.TimeField(
        #     widget=TimePicker(
        #         options={
        #             'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
        #             'defaultDate': '1970-01-01T14:56:00'
        #         },
        #         attrs={
        #             'input_toggle': True,
        #             'input_group': False,
        #         },
        #     ),
        # )
        # end_time = forms.TimeField(
        #     widget=TimePicker(
        #         options={
        #             'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
        #             'defaultDate': '1970-01-01T14:56:00'
        #         },
        #         attrs={
        #             'input_toggle': True,
        #             'input_group': False,
        #         },
        #     ),
        # )

        exclude = ("added_datetime",)


# CustomerAgentShift form used to do CRUD operations to CustomerAgentShift model
class CustomerAgentShiftForm(forms.ModelForm):
    class Meta:
        model = CustomerAgentShift
        fields = "__all__"


# CustomerAgent form used to do CRUD operations to CustomerAgent model
class CustomerAgentForm(forms.ModelForm):
    class Meta:
        model = CustomerAgent
        fields = "__all__"
        exclude = ("added_datetime", "last_modification_datetime",)


# CustomerPackage form used to do CRUD operations to CustomerPackage model
class CustomerPackageForm(forms.ModelForm):
    class Meta:
        model = CustomerPackage
        fields = "__all__"


# CustomerCall form used to do CRUD operations to CustomerCall model
class CustomerCallForm(forms.ModelForm):
    class Meta:
        model = CustomerCall
        fields = "__all__"


# CustomerPayment form used to do CRUD operations to CustomerPayment model
class CustomerPaymentForm(forms.ModelForm):
    class Meta:
        model = CustomerPayment
        fields = "__all__"


# CustomerAgentShiftsAttendant form used to do CRUD operations to CustomerAgentShiftsAttendant model
class CustomerAgentShiftsAttendantForm(forms.ModelForm):
    class Meta:
        model = CustomerAgentShiftsAttendant
        fields = "__all__"


# CustomerCallParticipant form used to do CRUD operations to CustomerCallParticipant model
class CustomerCallParticipantForm(forms.ModelForm):
    class Meta:
        model = CustomerCallParticipant
        fields = "__all__"


# CustomerPackageService form used to do CRUD operations to CustomerPackageService model
class CustomerPackageServiceForm(forms.ModelForm):
    class Meta:
        model = CustomerPackageService
        fields = "__all__"


# CustomerTeam form used to do CRUD operations to CustomerTeam model
class CustomerTeamForm(forms.ModelForm):
    class Meta:
        model = CustomerTeam
        fields = "__all__"
        exclude = ("added_datetime", "last_modification_datetime",)


# CustomerTelecomNumber form used to do CRUD operations to CustomerTelecomNumber model
class CustomerTelecomNumberForm(forms.ModelForm):
    class Meta:
        model = CustomerTelecomNumber
        fields = "__all__"


# BusinessTypeForm form used to do CRUD operations to CustomerTelecomNumber model
class BusinessTypeForm(forms.ModelForm):
    class Meta:
        model = BusinessType
        fields = "__all__"




