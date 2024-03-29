from django.urls import path
from .views import OulougLoginView, register_user
from django.contrib.auth.views import LogoutView

from apps.authentication.views import AddUserView
from apps.authentication.views import change_password
from django.contrib.admin.views.decorators import staff_member_required
from Util.static_strings import (NO_RECORDS_FOR_USER_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_USER_MODEL_ADMIN_MESSAGE,
                                 ADD_NEW_USER_TOOL_TIP_TEXT,
                                 UPDATE_USER_TOOL_TIP_TEXT,
                                 )
from apps.authentication.models import User
from apps.authentication.forms import SignUpForm,UserAdminForm,UserMonitorForm
from apps.authentication.views import UsersListView,UpdateUserView
urlpatterns = [
    path('login/', OulougLoginView.as_view(), name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('users/', staff_member_required(UsersListView.as_view(
        model=User,
        template_name="accounts/users/users_list.html",
        active_flag="user",
        main_active_flag="settings",
        model_name="User",
        no_records_admin=NO_RECORDS_FOR_USER_MODEL_ADMIN_MESSAGE,
        no_records_monitor=NO_RECORDS_FOR_USER_MODEL_MONITOR_MESSAGE,
        add_tool_tip_text=ADD_NEW_USER_TOOL_TIP_TEXT,
        update_tool_tip_text=UPDATE_USER_TOOL_TIP_TEXT,
        title="Users"
    ), login_url="login"), name="usersList"),
    path('users/addUsers', staff_member_required(AddUserView.as_view(
        model=User,
        form_class=SignUpForm,
        active_flag="user",
        main_active_flag="settings",
        reference_field_name="username",
        template_name="accounts/users/add_users.html",
        title="Add Users"
    ), login_url="login"), name="addUsers"),
    path('users/updateUser/<slug:slug>', staff_member_required(UpdateUserView.as_view(
        model=User,
        form_class=UserAdminForm,
        active_flag="user",
        main_active_flag="settings",
        reference_field_name="username",
        template_name="accounts/users/update_user.html",
        title = "Update User"
    ), login_url="login"), name="updateUser"),
    path('users/updateUserMonitor/<slug:slug>', staff_member_required(UpdateUserView.as_view(
        model=User,
        form_class=UserMonitorForm,
        active_flag="user",
        main_active_flag="settings",
        reference_field_name="username",
        template_name="accounts/users/update_user_monitor.html",
        title="Update User"
    ), login_url="login"), name="updateUserMonitor"),
    path('users/changePassword',change_password,name="changePassword")

]
