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
from django.views.generic.edit import UpdateView




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
        'country': 'active',
        'title': 'Add Countries'
    }




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
        'city': 'active',
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
        'state': 'active',
        'title': _('Add States')
    }



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
        form = CurrencyForm(request.POST)
        try:
            if self.form_valid(form):
                print("valid")
        except:
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
        'currency': 'active',
        'title': 'Add States'
    }



"""
ModelListView Class:
is a class used to list instances of a specified model,
it requires to define the following params:
- model (the model of the updated instance)
- template_name ( the path of the view that will be used)
- active_flag (this flag is used to add 'active' class to the current pages in sidebar) 
- model_name (this variable is used to specify model name for SearchMan class) 
- no_records_admin (this variable is used to specify the message that appears 
                     if there are no records for the admin user) 
- no_records_monitor (this variable is used to specify the message that appears 
                     if there are no records for the monitor user) 
- add_tool_tip_text (specifies the text that appears while hovering the 'add' button)
- update_tool_tip_text (specifies the text that appears while hovering the 'update' button)
"""
class ModelListView(ListView):
    model = None
    template_name = None
    active_flag = None
    model_name = None
    no_records_admin = None
    no_records_monitor = None
    add_tool_tip_text = None
    update_tool_tip_text = None
    # return default queryset used in this view
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

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
            'masters':'active',
            self.active_flag: "active",
            "no_records_admin": self.no_records_admin,
            "no_records_monitor": self.no_records_monitor,
            "add_tool_tip_text":self.add_tool_tip_text,
            "update_tool_tip_text":self.update_tool_tip_text,
            "instances_count":len(self.get_queryset()),

            # 'search': self.searchManObj.getSearch(),
            # 'search_result': self.search_result,
            # 'search_phrase': self.searchManObj.getSearchPhrase(),
            # 'search_option': self.searchManObj.getSearchOption(),
            # 'search_error': self.searchManObj.getSearchError(),
            'current_page': page,
        }
        return super().get(request)



"""
UpdateModelView Class:
is a class used to update instances of a specified model,
it requires to define the following params:
- model (the model of the updated instance)
- template_name ( the path of the view that will be used)
- active_flag (this flag is used to add 'active' class to the current pages in sidebar) 
"""
class UpdateModelView(UpdateView):
    model = None
    fields = "__all__"
    template_name = None
    active_flag = None
    def form_invalid(self, form):
        for field, items in form.errors.items():
            for item in items:
                print('{}: {}'.format(field, item))
        instance_name = form.cleaned_data['name']
        messages.error(self.request, f"{self.active_flag} <<{instance_name}>> did not updated , please try again!")
        return super(UpdateModelView, self).form_invalid(form)

    def form_valid(self, form):
        instance_name = form.cleaned_data['name']
        messages.success(self.request, f"{self.active_flag} <<{instance_name}>> updated successfully")
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.extra_context = {
            "masters": "active",
            self.active_flag: "active"
        }
        return super(UpdateModelView, self).get(self)

    def post(self, request, *args, **kwargs):
        self.extra_context = {
            "masters": "active",
            self.active_flag: "active"
        }
        return super(UpdateModelView, self).post(self)



