# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from locale import currency
from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from apps.authentication.models import User
# from . import Conutry , Currency , City , State , Teams , Services , Pakages

from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
#Thoses imports for group 
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib import messages

# from .forms import FormWithCaptcha


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))





# this views for the rest password and email done 



def password_reset_request(request):
    # ToDo: change options of message when deploying for testing in heroku
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'hysoca7@gmail.com', [user.email], fail_silently=False)                        # send_mail(
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("password_reset_done")


    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/reset_password.html", context={"password_reset_form":password_reset_form})
    


#This code for login from decorators and some dashborad view for admin site only 'oulgamin' and ashborad


'''


@unauthenticated_user
def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        """
        if user.is_staff:
            login(request, user)
            return redirect('http://127.0.0.1:8000/admin/login/?next=/admin/')
        """

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, ' Username OR Password is incorrect')
        
    context = {'form':form}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
#This for edit accounts for users 'Admin'

#we need edit form 

@login_required(login_url='login')
def editAccount(request):
    form    = EditAccountForm(instance=request.user)
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    
    context = {'form': form}
    return render(request, 'edit_account.html', context)

@login_required(login_url='login')
def home(request):
    conutries      = Conutry.objects.all()
    conutries_count = conutries.count()

    customers      = Customers.objects.all()
    customers_count = customers.count()


    
    teams      = Teams.objects.all()
    teams_count = teams.count()

    currencies       = Currency.objects.all()
    currencies_count  = currencies.count()

    cities        = City.objects.all()
    city_count   = cities.count()

    states       = State.objects.all()
    state_count  = states.count()

    context        = {'conutries_count':conutries_count, 'currencies_count':currencies_count, 'city_count':city_count, 'state_count':state_count}
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def allconutries(request):
    conutries      = Conutry.objects.all()
    context        = {'conutries':conutries}

    return render(request, 'allconutries.html', context)


@login_required(login_url='login')
def allcustomers(request):
    customers      = Customer.objects.all()
    context        = {'customers':customers}




@login_required(login_url='login')
def allteams(request):
    teams = Teams.objects.all()

    context   = {'teams':teams}
    return render(request, 'allteams.html', context)
#only admin can see this views 


@login_required(login_url='login')
@allowed_users(allowed_roles=['oulgadmin'])
def alltelcoms(request):
 
    return render(request, 'alltelcoms.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['oulgadmin'])
def allservices(request):
    services   = Services.objects.filter(oulgadmin=request.user.oulgadmin)
    context = {'services':services}

    return render(request, 'services.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['oulgadmin'])
def allpakages(request):
    pakages   = Pakages.objects.filter(oulgadmin=request.user.oulgadmin)
    context = {'pakages':pakages}

    return render(request, 'allpakages.html', context)



'''
