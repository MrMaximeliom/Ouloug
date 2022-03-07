from Util.utils import SearchMan
from .models import Country, City, State, Currency
from django.views.generic import ListView, FormView
from .forms import CountryForm, CityForm, StateForm, CurrencyForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from Util.static_strings import (NO_RECORDS_FOR_COUNTRY_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_COUNTRY_MODEL_ADMIN_MESSAGE, NO_RECORDS_FOR_CITY_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_CITY_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_STATE_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_STATE_MODEL_MONITOR_MESSAGE
                                 )
from Util.utils import OulougGroupPermission
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

"""
CountryListView:
This class is used to view all added countries in the system,
it allows only administrators and monitor users to  
access.
"""
class CountryListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = Country
    # specify the template in the view
    template_name = "address/countries/countries_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = "Countries"
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'masters': 'active',
        'countries': 'active',
        'no_records_admin': NO_RECORDS_FOR_COUNTRY_MODEL_ADMIN_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_COUNTRY_MODEL_MONITOR_MESSAGE
    }
    searchManObj = SearchMan("Country")

    # return default queryset used in this view
    def get_queryset(self):
        return Country.objects.all().order_by('-id')

    # def post(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     paginator = Paginator(queryset, 5)
    #     if request.POST.get('search_phrase') != '' and request.POST.get('search_options') == 'start_date':
    #         search_message = request.POST.get('search_phrase')
    #         self.search_result = Offer.objects.all().filter(
    #             name=search_message).order_by('-id')
    #         self.searchManObj.setPaginator(self.search_result)
    #         self.searchManObj.setSearchPhrase(search_message)
    #         self.searchManObj.setSearchOption('Offer Start Date')
    #         self.searchManObj.setSearchError(False)
    #     if 'clear' not in request.POST:
    #         self.searchManObj.setSearch(True)
    #     if request.POST.get('clear') == 'clear':
    #         offers = self.get_queryset()
    #         self.searchManObj.setPaginator(offers)
    #         self.searchManObj.setSearch(False)
    #     if request.GET.get('page'):
    #         # Grab the current page from query parameter consultant
    #         page = int(request.GET.get('page'))
    #     else:
    #         page = None
    #
    #     try:
    #         paginator = self.searchManObj.getPaginator()
    #         offers = paginator.page(page)
    #         # Create a page object for the current page.
    #     except PageNotAnInteger:
    #         # If the query parameter is empty then grab the first page.
    #         offers = paginator.page(1)
    #         page = 1
    #     except EmptyPage:
    #         # If the query parameter is greater than num_pages then grab the last page.
    #         offers = paginator.page(paginator.num_pages)
    #         page = paginator.num_pages
    #     self.extra_context = {
    #         'offers': 'active',
    #         self.active_flag: 'active',
    #         'page_range': paginator.page_range,
    #         'num_pages': paginator.num_pages,
    #         'offers_list': offers,
    #         'search': self.searchManObj.getSearch(),
    #         'search_result': self.search_result,
    #         'search_phrase': self.searchManObj.getSearchPhrase(),
    #         'search_option': self.searchManObj.getSearchOption(),
    #         'search_error': self.searchManObj.getSearchError(),
    #         'clear_search_tip': CLEAR_SEARCH_TIP,
    #         'search_offers_tip': SEARCH_OFFERS_TIP,
    #         'current_page': page,
    #         'title':self.title
    #     }
    #     return super().get(request)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, 5)
        if 'page' not in request.GET:
            countries = Country.objects.all().order_by('-id')
            self.searchManObj.setPaginator(countries)
            self.searchManObj.setSearch(False)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
            countries = paginator.page(page)
            # Create a page object for the current page.
        except PageNotAnInteger:
            # If the query parameter is empty then grab the first page.
            countries = paginator.page(1)
            page = 1
        except EmptyPage:
            # If the query parameter is greater than num_pages then grab the last page.
            countries = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        self.extra_context.update({
            'masters': 'active',
            'page_range': paginator.page_range,
            'num_pages': paginator.num_pages,
            'object_list': countries,
            # 'search': self.searchManObj.getSearch(),
            # 'search_result': self.search_result,
            # 'search_phrase': self.searchManObj.getSearchPhrase(),
            # 'search_option': self.searchManObj.getSearchOption(),
            # 'search_error': self.searchManObj.getSearchError(),
            'current_page': page,
            'title': self.title
        })
        return super().get(request)


"""
CountryFormView:
This class is used to represent the add country view , 
it allows only ouloug_admin users to access it
"""


class CountryFormView(OulougGroupPermission, FormView):
    # specify template name used to add new countries
    template_name = 'address/countries/add_countries.html'
    # specify the form used
    form_class = CountryForm
    # specify the page to return to after successfully adding new country
    success_url = 'countries'
    # specify user's groups allowed to access this view
    permission_required = ('administrator')

    # check if the form is valid or not after submitting it
    def post(self, request, *args, **kwargs):
        form = CountryForm(request.POST)
        if self.form_valid(form):
            print("valid")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
        return super().get(request)

    def form_valid(self, form):
        # return added country name
        country_name = self.request.POST['name']
        # save form data if form is valid
        form.save()
        # present success message to the user
        messages.success(self.request, f"Country <<{country_name}>> Added Successfully")
        # return the control to the original overridden function in the super class
        return super().form_valid(form)

    # priovided the required extra context for the view
    extra_context = {
        'masters': 'active',
        'countries': 'active',
        'add_offers': 'active',
        'title': 'Add Countries'
    }

"""
CityListView:
This class is used to view all added cities in the system,
it allows only administrators and monitor users to 
access.
"""


class CityListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = City
    # specify the template in the view
    template_name = "address/cities/cities_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = "Cities"
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'masters': 'active',
        'cities': 'active',
        'no_records_admin': NO_RECORDS_FOR_CITY_MODEL_ADMIN_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_CITY_MODEL_MONITOR_MESSAGE
    }
    searchManObj = SearchMan("City")

    # return default queryset used in this view
    def get_queryset(self):
        return City.objects.all().order_by('-id')

    # def post(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     paginator = Paginator(queryset, 5)
    #     if request.POST.get('search_phrase') != '' and request.POST.get('search_options') == 'start_date':
    #         search_message = request.POST.get('search_phrase')
    #         self.search_result = Offer.objects.all().filter(
    #             name=search_message).order_by('-id')
    #         self.searchManObj.setPaginator(self.search_result)
    #         self.searchManObj.setSearchPhrase(search_message)
    #         self.searchManObj.setSearchOption('Offer Start Date')
    #         self.searchManObj.setSearchError(False)
    #     if 'clear' not in request.POST:
    #         self.searchManObj.setSearch(True)
    #     if request.POST.get('clear') == 'clear':
    #         offers = self.get_queryset()
    #         self.searchManObj.setPaginator(offers)
    #         self.searchManObj.setSearch(False)
    #     if request.GET.get('page'):
    #         # Grab the current page from query parameter consultant
    #         page = int(request.GET.get('page'))
    #     else:
    #         page = None
    #
    #     try:
    #         paginator = self.searchManObj.getPaginator()
    #         offers = paginator.page(page)
    #         # Create a page object for the current page.
    #     except PageNotAnInteger:
    #         # If the query parameter is empty then grab the first page.
    #         offers = paginator.page(1)
    #         page = 1
    #     except EmptyPage:
    #         # If the query parameter is greater than num_pages then grab the last page.
    #         offers = paginator.page(paginator.num_pages)
    #         page = paginator.num_pages
    #     self.extra_context = {
    #         'offers': 'active',
    #         self.active_flag: 'active',
    #         'page_range': paginator.page_range,
    #         'num_pages': paginator.num_pages,
    #         'offers_list': offers,
    #         'search': self.searchManObj.getSearch(),
    #         'search_result': self.search_result,
    #         'search_phrase': self.searchManObj.getSearchPhrase(),
    #         'search_option': self.searchManObj.getSearchOption(),
    #         'search_error': self.searchManObj.getSearchError(),
    #         'clear_search_tip': CLEAR_SEARCH_TIP,
    #         'search_offers_tip': SEARCH_OFFERS_TIP,
    #         'current_page': page,
    #         'title':self.title
    #     }
    #     return super().get(request)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, 5)
        if 'page' not in request.GET:
            cities = City.objects.all().order_by('-id')
            self.searchManObj.setPaginator(cities)
            self.searchManObj.setSearch(False)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
            cities = paginator.page(page)
            # Create a page object for the current page.
        except PageNotAnInteger:
            # If the query parameter is empty then grab the first page.
            cities = paginator.page(1)
            page = 1
        except EmptyPage:
            # If the query parameter is greater than num_pages then grab the last page.
            cities = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        self.extra_context.update({
            'masters': 'active',
            'page_range': paginator.page_range,
            'num_pages': paginator.num_pages,
            'object_list': cities,
            # 'search': self.searchManObj.getSearch(),
            # 'search_result': self.search_result,
            # 'search_phrase': self.searchManObj.getSearchPhrase(),
            # 'search_option': self.searchManObj.getSearchOption(),
            # 'search_error': self.searchManObj.getSearchError(),
            'current_page': page,
            'title': self.title
        })
        return super().get(request)


"""
CityListView:
This class is used to view all added cities in the system,
it allows only administrators and monitor users to 
access.
"""


class CityListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = City
    # specify the template in the view
    template_name = "address/cities/cities_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = _("Cities")
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'masters': 'active',
        'cities': 'active',
        'no_records_admin': NO_RECORDS_FOR_CITY_MODEL_ADMIN_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_CITY_MODEL_MONITOR_MESSAGE
    }
    searchManObj = SearchMan("City")

    # return default queryset used in this view
    def get_queryset(self):
        return City.objects.all().order_by('-id')

    # def post(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     paginator = Paginator(queryset, 5)
    #     if request.POST.get('search_phrase') != '' and request.POST.get('search_options') == 'start_date':
    #         search_message = request.POST.get('search_phrase')
    #         self.search_result = Offer.objects.all().filter(
    #             name=search_message).order_by('-id')
    #         self.searchManObj.setPaginator(self.search_result)
    #         self.searchManObj.setSearchPhrase(search_message)
    #         self.searchManObj.setSearchOption('Offer Start Date')
    #         self.searchManObj.setSearchError(False)
    #     if 'clear' not in request.POST:
    #         self.searchManObj.setSearch(True)
    #     if request.POST.get('clear') == 'clear':
    #         offers = self.get_queryset()
    #         self.searchManObj.setPaginator(offers)
    #         self.searchManObj.setSearch(False)
    #     if request.GET.get('page'):
    #         # Grab the current page from query parameter consultant
    #         page = int(request.GET.get('page'))
    #     else:
    #         page = None
    #
    #     try:
    #         paginator = self.searchManObj.getPaginator()
    #         offers = paginator.page(page)
    #         # Create a page object for the current page.
    #     except PageNotAnInteger:
    #         # If the query parameter is empty then grab the first page.
    #         offers = paginator.page(1)
    #         page = 1
    #     except EmptyPage:
    #         # If the query parameter is greater than num_pages then grab the last page.
    #         offers = paginator.page(paginator.num_pages)
    #         page = paginator.num_pages
    #     self.extra_context = {
    #         'offers': 'active',
    #         self.active_flag: 'active',
    #         'page_range': paginator.page_range,
    #         'num_pages': paginator.num_pages,
    #         'offers_list': offers,
    #         'search': self.searchManObj.getSearch(),
    #         'search_result': self.search_result,
    #         'search_phrase': self.searchManObj.getSearchPhrase(),
    #         'search_option': self.searchManObj.getSearchOption(),
    #         'search_error': self.searchManObj.getSearchError(),
    #         'clear_search_tip': CLEAR_SEARCH_TIP,
    #         'search_offers_tip': SEARCH_OFFERS_TIP,
    #         'current_page': page,
    #         'title':self.title
    #     }
    #     return super().get(request)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, 5)
        if 'page' not in request.GET:
            cities = City.objects.all().order_by('-id')
            self.searchManObj.setPaginator(cities)
            self.searchManObj.setSearch(False)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
            cities = paginator.page(page)
            # Create a page object for the current page.
        except PageNotAnInteger:
            # If the query parameter is empty then grab the first page.
            cities = paginator.page(1)
            page = 1
        except EmptyPage:
            # If the query parameter is greater than num_pages then grab the last page.
            cities = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        self.extra_context.update({
            'masters': 'active',
            'page_range': paginator.page_range,
            'num_pages': paginator.num_pages,
            'object_list': cities,
            # 'search': self.searchManObj.getSearch(),
            # 'search_result': self.search_result,
            # 'search_phrase': self.searchManObj.getSearchPhrase(),
            # 'search_option': self.searchManObj.getSearchOption(),
            # 'search_error': self.searchManObj.getSearchError(),
            'current_page': page,
            'title': self.title
        })
        return super().get(request)


"""
CityFormView:
This class is used to represent the add city view , 
it allows only ouloug_admin users to access it
"""


class CityFormView(OulougGroupPermission, FormView):
    # specify template name used to add new countries
    template_name = 'address/cities/add_cities.html'
    # specify the form used
    form_class = CityForm
    # specify the page to return to after successfully adding new country
    success_url = 'cities'
    # specify user's groups allowed to access this view
    permission_required = ('administrator')

    # check if the form is valid or not after submitting it
    def post(self, request, *args, **kwargs):
        form = CityForm(request.POST)
        if self.form_valid(form):
            print("valid")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
        return super().get(request)

    def form_valid(self, form):
        # return added country name
        city_name = self.request.POST['name']
        # save form data if form is valid
        form.save()
        # present success message to the user
        messages.success(self.request, f"City <<{city_name}>> Added Successfully")
        # return the control to the original overridden function in the super class
        return super().form_valid(form)

    # priovided the required extra context for the view
    extra_context = {
        'masters': 'active',
        'cities': 'active',
        'title': _('Add Cities')
    }


"""
StateFormView:
This class is used to represent the add state view , 
it allows only ouloug_admin users to access it
"""


class StateFormView(OulougGroupPermission, FormView):
    # specify template name used to add new countries
    template_name = 'address/states/add_states.html'
    # specify the form used
    form_class = StateForm
    # specify the page to return to after successfully adding new country
    success_url = 'states'
    # specify user's groups allowed to access this view
    permission_required = ('administrator')

    # check if the form is valid or not after submitting it
    def post(self, request, *args, **kwargs):
        form = StateForm(request.POST)
        if self.form_valid(form):
            print("valid")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
        return super().get(request)

    def form_valid(self, form):
        # return added country name
        state_name = self.request.POST['name']
        # save form data if form is valid
        try:
            form.save()
            # present success message to the user
            messages.success(self.request, f"State <<{state_name}>> Added Successfully")
        except:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(self.request, '{}: {}'.format(field, item))

        # return the control to the original overridden function in the super class
        return super().form_valid(form)

    # priovided the required extra context for the view
    extra_context = {
        'masters': 'active',
        'states': 'active',
        'title': _('Add States')
    }


"""
StateListView:
This class is used to view all added states in the system,
it allows only administrators and monitor users to  
access.
"""


class StateListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = State
    # specify the template in the view
    template_name = "address/states/states_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = "States"
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'masters': 'active',
        'countries': 'active',
        'no_records_admin': NO_RECORDS_FOR_STATE_MODEL_ADMIN_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_STATE_MODEL_MONITOR_MESSAGE
    }
    searchManObj = SearchMan("State")

    # return default queryset used in this view
    def get_queryset(self):
        return State.objects.all().order_by('-id')

    # def post(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     paginator = Paginator(queryset, 5)
    #     if request.POST.get('search_phrase') != '' and request.POST.get('search_options') == 'start_date':
    #         search_message = request.POST.get('search_phrase')
    #         self.search_result = Offer.objects.all().filter(
    #             name=search_message).order_by('-id')
    #         self.searchManObj.setPaginator(self.search_result)
    #         self.searchManObj.setSearchPhrase(search_message)
    #         self.searchManObj.setSearchOption('Offer Start Date')
    #         self.searchManObj.setSearchError(False)
    #     if 'clear' not in request.POST:
    #         self.searchManObj.setSearch(True)
    #     if request.POST.get('clear') == 'clear':
    #         offers = self.get_queryset()
    #         self.searchManObj.setPaginator(offers)
    #         self.searchManObj.setSearch(False)
    #     if request.GET.get('page'):
    #         # Grab the current page from query parameter consultant
    #         page = int(request.GET.get('page'))
    #     else:
    #         page = None
    #
    #     try:
    #         paginator = self.searchManObj.getPaginator()
    #         offers = paginator.page(page)
    #         # Create a page object for the current page.
    #     except PageNotAnInteger:
    #         # If the query parameter is empty then grab the first page.
    #         offers = paginator.page(1)
    #         page = 1
    #     except EmptyPage:
    #         # If the query parameter is greater than num_pages then grab the last page.
    #         offers = paginator.page(paginator.num_pages)
    #         page = paginator.num_pages
    #     self.extra_context = {
    #         'offers': 'active',
    #         self.active_flag: 'active',
    #         'page_range': paginator.page_range,
    #         'num_pages': paginator.num_pages,
    #         'offers_list': offers,
    #         'search': self.searchManObj.getSearch(),
    #         'search_result': self.search_result,
    #         'search_phrase': self.searchManObj.getSearchPhrase(),
    #         'search_option': self.searchManObj.getSearchOption(),
    #         'search_error': self.searchManObj.getSearchError(),
    #         'clear_search_tip': CLEAR_SEARCH_TIP,
    #         'search_offers_tip': SEARCH_OFFERS_TIP,
    #         'current_page': page,
    #         'title':self.title
    #     }
    #     return super().get(request)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, 5)
        if 'page' not in request.GET:
            states = State.objects.all().order_by('-id')
            self.searchManObj.setPaginator(states)
            self.searchManObj.setSearch(False)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
            states = paginator.page(page)
            # Create a page object for the current page.
        except PageNotAnInteger:
            # If the query parameter is empty then grab the first page.
            states = paginator.page(1)
            page = 1
        except EmptyPage:
            # If the query parameter is greater than num_pages then grab the last page.
            states = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        self.extra_context.update({
            'masters': 'active',
            'page_range': paginator.page_range,
            'num_pages': paginator.num_pages,
            'object_list': states,
            # 'search': self.searchManObj.getSearch(),
            # 'search_result': self.search_result,
            # 'search_phrase': self.searchManObj.getSearchPhrase(),
            # 'search_option': self.searchManObj.getSearchOption(),
            # 'search_error': self.searchManObj.getSearchError(),
            'current_page': page,
            'title': self.title
        })
        return super().get(request)


"""
CurrencyFormView:
This class is used to represent the add state view , 
it allows only ouloug_admin users to access it
"""


class CurrencyFormView(OulougGroupPermission, FormView):
    # specify template name used to add new currencies
    template_name = 'address/currencies/add_currencies.html'
    # specify the form used
    form_class = CurrencyForm
    # specify the page to return to after successfully adding new currency
    success_url = 'currencies'
    # specify user's groups allowed to access this view
    permission_required = ('administrator')

    # check if the form is valid or not after submitting it
    def post(self, request, *args, **kwargs):
        form = CountryForm(request.POST)
        if self.form_valid(form):
            print("valid")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
        return super().get(request)

    def form_valid(self, form):
        # return added currency name
        currency_name = self.request.POST['name']
        # save form data if form is valid
        form.save()
        # present success message to the user
        messages.success(self.request, f"Currency {currency_name} Added Successfully")
        # return the control to the original overridden function in the super class
        return super().form_valid(form)

    # priovided the required extra context for the view
    extra_context = {
        'masters': 'active',
        'currencies': 'active',
        'title': 'Add States'
    }


"""
CurrencyListView:
This class is used to view all added states in the system,
it allows only administrators and monitor users to  
access.
"""


class CurrencyListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = Currency
    # specify the template in the view
    template_name = "address/currencies/currencies_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = "Currencies"
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'masters': 'active',
        'currencies': 'active',
        'no_records_admin': NO_RECORDS_FOR_STATE_MODEL_ADMIN_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_STATE_MODEL_MONITOR_MESSAGE
    }
    searchManObj = SearchMan("State")

    # return default queryset used in this view
    def get_queryset(self):
        return Currency.objects.all().order_by('-id')

    # def post(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     paginator = Paginator(queryset, 5)
    #     if request.POST.get('search_phrase') != '' and request.POST.get('search_options') == 'start_date':
    #         search_message = request.POST.get('search_phrase')
    #         self.search_result = Offer.objects.all().filter(
    #             name=search_message).order_by('-id')
    #         self.searchManObj.setPaginator(self.search_result)
    #         self.searchManObj.setSearchPhrase(search_message)
    #         self.searchManObj.setSearchOption('Offer Start Date')
    #         self.searchManObj.setSearchError(False)
    #     if 'clear' not in request.POST:
    #         self.searchManObj.setSearch(True)
    #     if request.POST.get('clear') == 'clear':
    #         offers = self.get_queryset()
    #         self.searchManObj.setPaginator(offers)
    #         self.searchManObj.setSearch(False)
    #     if request.GET.get('page'):
    #         # Grab the current page from query parameter consultant
    #         page = int(request.GET.get('page'))
    #     else:
    #         page = None
    #
    #     try:
    #         paginator = self.searchManObj.getPaginator()
    #         offers = paginator.page(page)
    #         # Create a page object for the current page.
    #     except PageNotAnInteger:
    #         # If the query parameter is empty then grab the first page.
    #         offers = paginator.page(1)
    #         page = 1
    #     except EmptyPage:
    #         # If the query parameter is greater than num_pages then grab the last page.
    #         offers = paginator.page(paginator.num_pages)
    #         page = paginator.num_pages
    #     self.extra_context = {
    #         'offers': 'active',
    #         self.active_flag: 'active',
    #         'page_range': paginator.page_range,
    #         'num_pages': paginator.num_pages,
    #         'offers_list': offers,
    #         'search': self.searchManObj.getSearch(),
    #         'search_result': self.search_result,
    #         'search_phrase': self.searchManObj.getSearchPhrase(),
    #         'search_option': self.searchManObj.getSearchOption(),
    #         'search_error': self.searchManObj.getSearchError(),
    #         'clear_search_tip': CLEAR_SEARCH_TIP,
    #         'search_offers_tip': SEARCH_OFFERS_TIP,
    #         'current_page': page,
    #         'title':self.title
    #     }
    #     return super().get(request)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, 5)
        if 'page' not in request.GET:
            states = Currency.objects.all().order_by('-id')
            self.searchManObj.setPaginator(states)
            self.searchManObj.setSearch(False)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
            states = paginator.page(page)
            # Create a page object for the current page.
        except PageNotAnInteger:
            # If the query parameter is empty then grab the first page.
            states = paginator.page(1)
            page = 1
        except EmptyPage:
            # If the query parameter is greater than num_pages then grab the last page.
            states = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        self.extra_context.update({
            'masters': 'active',
            'page_range': paginator.page_range,
            'num_pages': paginator.num_pages,
            'object_list': states,
            # 'search': self.searchManObj.getSearch(),
            # 'search_result': self.search_result,
            # 'search_phrase': self.searchManObj.getSearchPhrase(),
            # 'search_option': self.searchManObj.getSearchOption(),
            # 'search_error': self.searchManObj.getSearchError(),
            'current_page': page,
            'title': self.title
        })
        return super().get(request)
