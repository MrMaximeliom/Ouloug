from Util.utils import SearchMan

from apps.teams.models import Team
from apps.telecoms.forms import TelcomOperatorForm, TelecomNumberForm
from .models import TelecomNumber, TelecomOperator
from django.views.generic import ListView, FormView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from Util.static_strings import (
                                 NO_RECORDS_FOR_TELECOMS_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_TELECOMS_MODEL_MONITOR_MESSAGE
                                 )
from Util.utils import OulougGroupPermission
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


"""
TelecomsFormView:
This class is used to represent the add Telcoms view , 
it allows only ouloug_admin users to access it
"""


class TelecomsFormView(OulougGroupPermission, FormView):
    # specify template name used to add new telecoms
    template_name = 'telecoms/add_telecoms.html'
    # specify the form used
    form_class = TelcomOperatorForm
    # specify the page to return to after successfully adding new telecoms
    success_url = 'telecoms'
    # specify user's groups allowed to access this view
    permission_required = ('administrator')

    # check if the form is valid or not after submitting it
    def post(self, request, *args, **kwargs):
        form = TelcomOperatorForm(request.POST)
        if self.form_valid(form):
            print("valid")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
        return super().get(request)

    def form_valid(self, form):
        # return added team name
        name = self.request.POST['name']
        # save form data if form is valid
        form.save()
        # present success message to the user
        messages.success(self.request, f"Telecoms {name} Added Successfully")
        # return the control to the original overridden function in the super class
        return super().form_valid(form)

    # priovided the required extra context for the view
    extra_context = {
        'masters': 'active',
        'telecoms': 'active',
        'title': 'Add Telecoms'
    }


"""
TelecomsListView:
This class is used to view all added telecoms in the system,
it allows only administrators and monitor users to  
access.
"""


class TelecomsListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = TelecomOperator
    # specify the template in the view
    template_name = "telecoms/telecoms_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = "telecoms"
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'masters': 'active',
        'telecoms': 'active',
        'no_records_admin': NO_RECORDS_FOR_TELECOMS_MODEL_ADMIN_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_TELECOMS_MODEL_MONITOR_MESSAGE
    }
    searchManObj = SearchMan("Telcoms")

    # return default queryset used in this view
    def get_queryset(self):
        return TelecomOperator.objects.all().order_by('-id')

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
            telecoms = Team.objects.all().order_by('-id')
            self.searchManObj.setPaginator(telecoms)
            self.searchManObj.setSearch(False)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
            telecoms = paginator.page(page)
            # Create a page object for the current page.
        except PageNotAnInteger:
            # If the query parameter is empty then grab the first page.
            telecoms = paginator.page(1)
            page = 1
        except EmptyPage:
            # If the query parameter is greater than num_pages then grab the last page.
            telecoms = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        self.extra_context.update({
            'masters': 'active',
            'telecoms': 'active',
            'page_range': paginator.page_range,
            'num_pages': paginator.num_pages,
            'object_list': telecoms,
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
TelecomNumberFormView:
This class is used to represent the add Telcoms view , 
it allows only ouloug_admin users to access it
"""


class TelecomNumberFormView(OulougGroupPermission, FormView):
    # specify template name used to add new telecoms
    template_name = 'telecom_number/add_telecom_number.html'
    # specify the form used
    form_class = TelecomNumberForm
    # specify the page to return to after successfully adding new telecoms
    success_url = 'telecomNumber'
    # specify user's groups allowed to access this view
    permission_required = ('administrator')

    # check if the form is valid or not after submitting it
    def post(self, request, *args, **kwargs):
        form = TelecomNumberForm(request.POST)
        if self.form_valid(form):
            print("valid")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
        return super().get(request)

    def form_valid(self, form):
        # return added team name
        name = self.request.POST['name']
        # save form data if form is valid
        form.save()
        # present success message to the user
        messages.success(self.request, f"Telecom number {name} Added Successfully")
        # return the control to the original overridden function in the super class
        return super().form_valid(form)

    # priovided the required extra context for the view
    extra_context = {
        'ouloug_services': 'active',
        'telecom_number': 'active',
        'title': 'Add Telecom Number'
    }


"""
TelecomNumberListView:
This class is used to view all added telecom number in the system,
it allows only administrators and monitor users to  
access.
"""


class TelecomNumberListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = TelecomNumber
    # specify the template in the view
    template_name = "telecom_number/telecom_number_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = "Telecomphone"
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'ouloug_services': 'active',
        'telecom_number': 'active',
        'no_records_admin': NO_RECORDS_FOR_TELECOMS_MODEL_ADMIN_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_TELECOMS_MODEL_MONITOR_MESSAGE
    }
    searchManObj = SearchMan("Telecom Phone Number")

    # return default queryset used in this view
    def get_queryset(self):
        return TelecomNumber.objects.all().order_by('-id')

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
            states = Team.objects.all().order_by('-id')
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
            'telecom_number': 'active',
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

