from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib import messages
from Util.utils import SearchMan
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from Util.static_strings import (
    FIRST_NAME_EMPTY_ERROR,
    FIRST_NAME_SYNTAX_ERROR,
    SECOND_NAME_SYNTAX_ERROR,
    SECOND_NAME_EMPTY_ERROR,
    THIRD_NAME_EMPTY_ERROR,
    THIRD_NAME_SYNTAX_ERROR,
    FOURTH_NAME_EMPTY_ERROR,
    FOURTH_NAME_SYNTAX_ERROR,
    USERNAME_EMPTY_ERROR,
    USERNAME_BAD_FORMAT,
    PHONE_PHONE_EMPTY_ERROR,
    PHONE_NUMBER_SYNTAX_ERROR,
    EMAIL_EMPTY_ERROR,
    EMAIL_SYNTAX_ERROR,
    PASSWORD_EMPTY_ERROR,
    PASSWORDS_NOT_MATCH,
    CONFIRM_PASSWORD_EMPTY_ERROR
)
from .forms import SignUpForm


class OulougLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    from apps.authentication.forms import UserLoginForm
    # from Util.handle_login_form_strings import USERNAME_EMPTY_ERROR,USERNAME_BAD_FORMAT,PASSWORD_EMPTY_ERROR
    form_class = UserLoginForm
    success_url = ""

    def form_valid(self, form):
        from django.contrib.auth import login as auth_login
        from django.http import HttpResponseRedirect
        """Security check complete. Log the user in."""
        current_user = form.get_user()
        if current_user.staff:
            auth_login(self.request, form.get_user())
            username = str(current_user)
            messages.success(self.request, f" Welcome {username} Have a nice day")
            return HttpResponseRedirect(self.get_success_url())
        else:
            print("current user is: ", current_user)
            messages.error(self.request, 'Phone Number or Password Error for Staff User')

        return redirect('login')

    extra_context = {
        'title': 'Login Page',
        'invalid_login': 'Phone Number or Password Error for Admin Or Monitor User',
        'hide_footer': True,

    }


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('first password', user.password)
            user.set_password(user.password)
            print("\nafter hashing:", user.password)
            user.save()
            messages.success(request, "You have successfully registered, log in!")

            return redirect("login")
        else:
            messages.error(request, "Please Make Sure That Your Data is Valid!")

            for field, items in form.errors.items():
                for item in items:
                    print('{}: {}'.format(field, item))
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form,
                                                      'data_js': {
                                                          "first_name_empty_error": FIRST_NAME_EMPTY_ERROR,
                                                          "second_name_empty_error": SECOND_NAME_EMPTY_ERROR,
                                                          "third_name_empty_error": THIRD_NAME_EMPTY_ERROR,
                                                          "fourth_name_empty_error": FOURTH_NAME_EMPTY_ERROR,
                                                          "first_name_error": FIRST_NAME_SYNTAX_ERROR,
                                                          "second_name_error": SECOND_NAME_SYNTAX_ERROR,
                                                          "third_name_error": THIRD_NAME_SYNTAX_ERROR,
                                                          "fourth_name_error": FOURTH_NAME_SYNTAX_ERROR,
                                                          "email_empty_error": EMAIL_EMPTY_ERROR,
                                                          "email_error": EMAIL_SYNTAX_ERROR,
                                                          "username_empty_error": USERNAME_EMPTY_ERROR,
                                                          "username_error": USERNAME_BAD_FORMAT,
                                                          "phone_number_empty_error": PHONE_PHONE_EMPTY_ERROR,
                                                          "phone_number_error": PHONE_NUMBER_SYNTAX_ERROR,
                                                          "passwords_not_match": PASSWORDS_NOT_MATCH,
                                                          "password_empty_error": PASSWORD_EMPTY_ERROR,
                                                          "confirm_password_empty_error": CONFIRM_PASSWORD_EMPTY_ERROR

                                                      }
                                                      })


@staff_member_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changePassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/users/change_password.html', {
        'form': form,
        'settings': 'active',
        'change_password': 'active'

    })


"""
AddModelView Class:
is a class used to add instances of a specified model,
it requires to define the following params:
- model (the model to add new instances)
- template_name ( the path of the view that will be used)
- active_flag (this flag is used to add 'active' class to the current pages in sidebar) 
- reference_field_name (this field used to reference the field that will be used in success/error messages) 
- main_active_flag (this flag is used to add 'active' class to the main master current pages in sidebar)
- title (specifies the page's title)
"""


class AddUserView(CreateView):
    model = None
    fields = None
    template_name = None
    active_flag = None
    reference_field_name = None
    main_active_flag = None
    title = None

    def form_invalid(self, form):
        for field, items in form.errors.items():
            for item in items:
                print('{}: {}'.format(field, item))
        instance_name = form.cleaned_data[self.reference_field_name]
        messages.error(self.request, f"{self.active_flag} <<{instance_name}>> did not added , please try again!")
        return super(AddUserView, self).form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        instance_name = form.cleaned_data[self.reference_field_name]
        self.object.added_by = self.request.user
        self.object.set_password(self.object.password)
        self.object.save()
        messages.success(self.request, f"{self.active_flag} <<{instance_name}>> added successfully")
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.extra_context = {
            self.main_active_flag: "active",
            self.active_flag: "active",
            "title": self.title
        }
        return super(AddUserView, self).get(self)

    def post(self, request, *args, **kwargs):
        self.extra_context = {
            self.main_active_flag: "active",
            self.active_flag: "active",
            "title": self.title
        }
        return super(AddUserView, self).post(self)


class UsersListView(ListView):
    model = None
    template_name = None
    main_active_flag = None
    active_flag = None
    model_name = None
    no_records_admin = None
    no_records_monitor = None
    add_tool_tip_text = None
    update_tool_tip_text = None
    title = None
    searchManObj = SearchMan(model_name)

    # return default queryset used in this view
    def get_queryset(self):
        from apps.authentication.models import User
        if self.request.user.user_type == "monitor":
           return User.objects.filter(username=self.request.user.username)
        else:
            return User.objects.all().order_by('-id')





    def get(self, request, *args, **kwargs):
        from apps.authentication.models import User
        print(self.request.user)
        searchManObj = SearchMan(self.model_name)
        queryset = self.get_queryset()
        paginator = Paginator(queryset, 5)
        if 'page' not in request.GET:
            instances = self.model.objects.all().order_by('-id')
            searchManObj.setPaginator(instances)
            searchManObj.setSearch(False)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = searchManObj.getPaginator()
            instances = paginator.page(page)
            # Create a page object for the current page.
        except PageNotAnInteger:
            # If the query parameter is empty then grab the first page.
            instances = paginator.page(1)
            page = 1
        except EmptyPage:
            # If the query parameter is greater than num_pages then grab the last page.
            instances = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        self.extra_context = {
            'page_range': paginator.page_range,
            'num_pages': paginator.num_pages,
            'object_list': instances,
            'user_data': User.objects.filter(username=self.request.user.username),
            self.main_active_flag: 'active',
            self.active_flag: "active",
            "no_records_admin": self.no_records_admin,
            "no_records_monitor": self.no_records_monitor,
            "add_tool_tip_text": self.add_tool_tip_text,
            "update_tool_tip_text": self.update_tool_tip_text,
            "instances_count": len(self.get_queryset()),
            'current_page': page,
            'title': self.title
        }
        return super().get(request)

class UpdateUserView(UpdateView):
    model = None
    fields = None
    template_name = None
    active_flag = None
    reference_field_name = None
    main_active_flag = None
    title = None

    def form_invalid(self, form):
        for field, items in form.errors.items():
            for item in items:
                print('{}: {}'.format(field, item))
        instance_name = form.cleaned_data[self.reference_field_name]
        messages.error(self.request, f"{self.active_flag} <<{instance_name}>> did not updated , please try again!")
        return super(UpdateUserView, self).form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        instance_name = form.cleaned_data[self.reference_field_name]
        messages.success(self.request, f"{self.active_flag} <<{instance_name}>> updated successfully")
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.extra_context = {
            self.main_active_flag: "active",
            self.active_flag: "active",
            "title": self.title,
        }
        return super(UpdateUserView, self).get(self)

    def post(self, request, *args, **kwargs):
        self.extra_context = {
            self.main_active_flag: "active",
            self.active_flag: "active",
            "title": self.title
        }
        return super(UpdateUserView, self).post(self)