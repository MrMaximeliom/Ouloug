# from django.contrib.auth.mixins import PermissionRequiredMixin


class EnablePartialUpdateMixin:
    """Enable partial updates

    Override partial kwargs in UpdateModelMixin class
    https://github.com/encode/django-rest-framework/blob/91916a4db14cd6a06aca13fb9a46fc667f6c0682/rest_framework/mixins.py#L64
    """

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
import datetime
from django.core.validators import MaxValueValidator
import string
import random


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


def rand_slug():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%S")
    import datetime
    today = datetime.date.today()
    unique_list = list( ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))+str(current_time)+str(today))
    random.shuffle(unique_list)
    return ''.join(unique_list)


SMS_USERNAME = 'uniseal'
SMS_PASSWORD = '823178'


def check_string_search_phrase(search_phrase):
    import re
    temp_holder = search_phrase
    special_char = re.findall(r'\W', temp_holder.replace(" ", ""))
    # returns true if search_phrase contains special chars and returns search_phrase without leading spaces
    return len(special_char) > 0, search_phrase.strip()


# TODO add logic to this function to use it later in the search functionality

def check_phone_number(phone):
    import re
    default_regex = r'^9\d{8}$|^1\d{8}$'
    another_regex = r'^09\d{8}$|^01\d{8}$'
    if re.findall(default_regex, phone):
        return True, re.findall(default_regex, phone)[0]
    elif re.findall(another_regex, phone):
        return True, re.findall(another_regex, phone)[0][1:]
    else:
        return False, ''


class SearchMan:
    search_error = False
    queryset = None

    def __init__(self, model):
        from django.core.paginator import Paginator
        if model == "Country":
            from apps.address.models import Country
            countries = Country.objects.all().order_by("id")
            self.set_querySet(countries)
            self.paginator = Paginator(countries, 5)
        if model == "City":
            from apps.address.models import City
            cities = City.objects.all().order_by("id")
            self.set_querySet(cities)
            self.paginator = Paginator(cities, 5)
        if model == "State":
            from apps.address.models import State
            states = State.objects.all().order_by("id")
            self.set_querySet(states)
            self.paginator = Paginator(states, 5)
        if model == "Service":
            from apps.services.models import Service
            services = Service.objects.all().order_by("id")
            self.set_querySet(services)
            self.paginator = Paginator(services, 5)
        if model == "Package":
            from apps.packages.models import Package
            packages = Package.objects.all().order_by("id")
            self.set_querySet(packages)
            self.paginator = Paginator(packages, 5)
        if model == "BusinessType":
            from apps.customers.models import BusinessType
            business_types = BusinessType.objects.all().order_by("id")
            self.set_querySet(business_types)
            self.paginator = Paginator(business_types, 5)
        if model == "Team":
            from apps.teams.models import Team
            teams = Team.objects.all().order_by("id")
            self.set_querySet(teams)
            self.paginator = Paginator(teams, 5)
        if model == "AgentShift":
            from apps.customers.models import AgentShift
            agent_shifts = AgentShift.objects.all().order_by("id")
            self.set_querySet(agent_shifts)
            self.paginator = Paginator(agent_shifts, 5)
        if model == "CustomerCall":
            from apps.customers.models import CustomerCall
            customer_calls = CustomerCall.objects.all().order_by("id")
            self.set_querySet(customer_calls)
            self.paginator = Paginator(customer_calls, 5)
        if model == "TelecomOperator":
            from apps.telecoms.models import TelecomOperator
            telecoms = TelecomOperator.objects.all().order_by("id")
            self.set_querySet(telecoms)
            self.paginator = Paginator(telecoms, 5)
        if model == "TelecomNumber":
            from apps.telecoms.models import TelecomNumber
            telecom_numbers = TelecomNumber.objects.all().order_by("id")
            self.set_querySet(telecom_numbers)
            self.paginator = Paginator(telecom_numbers, 5)
        if model == "CustomerPayment":
            from apps.customers.models import CustomerPayment
            customer_payments = CustomerPayment.objects.all().order_by("id")
            self.set_querySet(customer_payments)
            self.paginator = Paginator(customer_payments, 5)
        if model == "User":
            from apps.authentication.models import User
            users = User.objects.all().order_by("id")
            self.set_querySet(users)
            self.paginator = Paginator(users, 5)
        if model == "Customer":
            from apps.customers.models import Customer
            customers = Customer.objects.all().order_by("id")
            self.set_querySet(customers)
            self.paginator = Paginator(customers, 5)

    def setPaginator(self, query):
        from django.core.paginator import Paginator
        self.paginator = Paginator(query, 5)

    def getPaginator(self):
        return self.paginator

    def set_querySet(self,queryset):
        self.queryset = queryset

    def get_queryset(self):
        return self.queryset

    search = False
    search_phrase = ''
    search_option = ''

    def setSearch(self, flag):
        self.search = flag

    def getSearch(self):
        return self.search

    def setSearchPhrase(self, phrase):
        self.search_phrase = phrase

    def getSearchPhrase(self):
        return self.search_phrase

    def setSearchOption(self, option):
        self.search_option = option

    def getSearchOption(self):
        return self.search_option

    def setSearchError(self, bool):
        self.search_error = bool

    def getSearchError(self):
        return self.search_error


"""
OulougGroupPermission Class:
This class is used to specify allowed user types for system models
"""


# class OulougGroupPermission(PermissionRequiredMixin):
#     # by default allow only users of ouloug_admin and ouloug_monitor
#     #  to access the countries' pages
#     permission_required = ('administrator', 'monitor')
#
#     # check if the logged-in user has the access permission or not
#     def has_permission(self):
#         user_types = self.get_permission_required()
#         # check user type
#         for user_type in user_types:
#             if self.request.user.is_authenticated:
#                 if self.request.user.user_type == user_type:
#                     return True
#             else:
#                 return redirect('login')

        # groups = self.get_permission_required()
        # user_groups = self.request.user.groups.values('name')
        # for group in groups:
        #     for user_group in user_groups:
        #         if user_group['name'] == group:
        #             return True

def random_id(letter_count, digit_count):
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    import datetime
    today = datetime.date.today()
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))

    sam_list = list(str1)  # it converts the string to list.
    random.shuffle(sam_list)  # It uses a random.shuffle() function to shuffle the string.
    final_string = ''.join(sam_list)
    return "id-" + final_string + "-" + current_time + "-" + str(today)