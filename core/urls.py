# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.contrib.auth import views as auth_views #import this


admin.site.site_title  = "Ouloug Administration"
admin.site.site_header = "Ouloug Administration"
admin.site.index_title = "Ouloug Administration"



urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route

    # path("", include("captcha_runner.urls")),


    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),
    path("", include("apps.address.urls")),
    path("", include("apps.services.urls")),
    path("", include("apps.customers.urls")),
    path("", include("apps.teams.urls")),
    path("", include("apps.packages.urls")),
    path("", include("apps.customers.urls")),
    path("", include("apps.telecoms.urls")),
    # url for change password
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html',
                                                                   success_url='/'
                                                                   ),
         name='change_password'
         ),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete')
    # UI Kits Html files
]
handler404 = 'apps.error_handler.views.error_404'
handler500 = 'apps.error_handler.views.error_500'
handler403 = 'apps.error_handler.views.error_403'
handler400 = 'apps.error_handler.views.error_400'