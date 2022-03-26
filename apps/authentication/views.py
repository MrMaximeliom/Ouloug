from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib import messages
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
from django.contrib.auth import views as auth_views


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
        print("here")
        if current_user.staff:
            auth_login(self.request, form.get_user())
            username = str(current_user)
            messages.success(self.request, f" Welcome {username} Have a nice day")
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(self.request, 'Phone Number or Password Error for Staff User')

        return redirect('login')

    extra_context = {
        'title': 'Login Page',
        'invalid_login': 'Phone Number or Password Error for Admin Or Monitor User',
        'hide_footer': True,

    }
def login_view(request):
    form = LoginForm(request.POST)
    msg = None
    if request.method == "POST":

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {user.username} have a nice day!")
                return redirect("home")
            else:
                messages.error(request, "Invalid Credentials")
        else:
            msg = 'Error validating the form'
            for field, items in form.errors.items():
                for item in items:
                    print('{}: {}'.format(field, item))

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


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
