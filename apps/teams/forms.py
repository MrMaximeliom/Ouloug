from django import forms
from apps.teams.models import Team
# TeamForm form used to do CRUD operations to Team model
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"