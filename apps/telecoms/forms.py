from django import forms
from apps.telecoms.models import TelecomNumber,TelecomOperator
# TeamForm form used to do CRUD operations to Team model
class TelcomOperatorForm(forms.ModelForm):
    class Meta:
        model = TelecomOperator
        fields = "__all__"




class TelecomNumberForm(forms.ModelForm):
    class Meta:
        model = TelecomNumber
        fields = "__all__"








