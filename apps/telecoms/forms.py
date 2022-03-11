from django import forms
from apps.telecoms.models import Team
# TeamForm form used to do CRUD operations to Team model
class TelcomForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"




class TelecomphoneForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"








