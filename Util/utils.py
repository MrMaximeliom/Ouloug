from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect


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
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
SMS_USERNAME = 'uniseal'
SMS_PASSWORD = '823178'
def check_string_search_phrase(search_phrase):
    import re
    temp_holder = search_phrase
    special_char = re.findall(r'\W', temp_holder.replace(" ", ""))
    # returns true if search_phrase contains special chars and returns search_phrase without leading spaces
    return len(special_char) > 0 , search_phrase.strip()
# TODO add logic to this function to use it later in the search functionality

def check_phone_number(phone):
    import re
    default_regex = r'^9\d{8}$|^1\d{8}$'
    another_regex = r'^09\d{8}$|^01\d{8}$'
    if re.findall(default_regex, phone):
        return True,re.findall(default_regex,phone)[0]
    elif re.findall(another_regex,phone):
        return True, re.findall(another_regex,phone)[0][1:]
    else:
        return False,''

class SearchMan:
    search_error = False

    def __init__(self,model):
        from django.core.paginator import Paginator
        from django.db.models import Count
        if model == "Country":
            from apps.address.models import Country
            countries = Country.objects.all().order_by("id")
            self.paginator = Paginator(countries, 5)
        if model == "City":
            from apps.address.models import City
            cities = City.objects.all().order_by("id")
            self.paginator = Paginator(cities, 5)
        if model == "State":
            from apps.address.models import State
            states = State.objects.all().order_by("id")
            self.paginator = Paginator(states, 5)
        if model == "Service":
            from apps.services.models import Service
            services = Service.objects.all().order_by("id")
            self.paginator = Paginator(services, 5)
        if model == "BusinessType":
            from apps.customers.models import BusnessType
            business_types = BusnessType.objects.all().order_by("id")
            self.paginator = Paginator(business_types, 5)
        if model == "Team":
            from apps.teams.models import Team
            teams = Team.objects.all().order_by("id")
            self.paginator = Paginator(teams, 5)
        if model == "AgentShift":
            from apps.customers.models import AgentShift
            agentShifts = AgentShift.objects.all().order_by("id")
            self.paginator = Paginator(agentShifts, 5)





    def setPaginator(self,query):
        from django.core.paginator import Paginator
        self.paginator = Paginator(query, 60)

    def getPaginator(self):
        return self.paginator
    search = False
    search_phrase = ''
    search_option = ''
    def setSearch(self,bool):
        self.search = bool
    def getSearch(self):
        return self.search
    def setSearchPhrase(self,phrase):
        self.search_phrase = phrase
    def getSearchPhrase(self):
        return  self.search_phrase
    def setSearchOption(self, option):
        self.search_option = option
    def getSearchOption(self):
        return self.search_option
    def setSearchError(self,bool):
        self.search_error=bool
    def getSearchError(self):
        return self.search_error

"""
OulougGroupPermission Class:
This class is used to specify allowed user types for system models
"""


class OulougGroupPermission(PermissionRequiredMixin):
    # by default allow only users of ouloug_admin and ouloug_monitor
    #  to access the countries' pages
    permission_required = ('administrator', 'monitor')

    # check if the logged-in user has the access permission or not
    def has_permission(self):
        user_types = self.get_permission_required()
        # check user type
        for user_type in user_types:
            if self.request.user.is_authenticated:
                if self.request.user.user_type == user_type:
                    return True
            else:
                return redirect('login')

        # groups = self.get_permission_required()
        # user_groups = self.request.user.groups.values('name')
        # for group in groups:
        #     for user_group in user_groups:
        #         if user_group['name'] == group:
        #             return True
