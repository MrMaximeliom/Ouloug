from django import forms
from apps.packages.models import Package,PackageService,PackageBillingType

# Package form used to do CRUD operations to Package model
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = "__all__"
        exclude = ("added_datetime","last_modification_datetime",)

# PackageService form used to do CRUD operations to PackageService model
class PackageServiceForm(forms.ModelForm):
    class Meta:
        model = PackageService
        fields = "__all__"
        exclude = ("added_datetime","last_modification_datetime",)


# PackageBillingType form used to do CRUD operations to PackageBillingType model
class PackageBillingTypeForm(forms.ModelForm):
    class Meta:
        model = PackageBillingType
        fields = "__all__"
        exclude = ("added_datetime","last_modification_datetime",)

