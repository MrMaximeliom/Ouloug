from django.urls import path
from apps.packages.views import (PackageListView,PackageFormView,
                               changePackageStatus )
urlpatterns = [
    path('packages/', PackageListView.as_view(), name="packagesList"),
    path('packages/addPackages', PackageFormView.as_view(), name="addPackages"),
    path('packages/changePackageStatus/<int:pk><str:status>',changePackageStatus , name="changePackageStatus"),
]
