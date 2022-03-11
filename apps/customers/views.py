from django.shortcuts import render



from Util.utils import SearchMan
from apps.customers.forms import BusinessTypeForm,AgentShiftForm
from .models import BusnessType,AgentShift
from django.views.generic import ListView, FormView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from Util.static_strings import (
                                 NO_RECORDS_FOR_BUSINESS_TYPE_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_BUSINESS_TYPE_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_AGENT_SHIFT_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_AGENT_SHIFT_MODEL_MONITOR_MESSAGE

                                 )
from Util.utils import OulougGroupPermission
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.




"""
Business Type FormView:
This class is used to represent the add state view , 
it allows only ouloug_admin users to access it
"""

class BusinessFormView(OulougGroupPermission, FormView):
    # specify template name used to add new business_type
    template_name = 'business_type/add_business_type.html'
    # specify the form used
    form_class = BusinessTypeForm
    # specify the page to return to after successfully adding new currency
    success_url = 'business'
    # specify user's groups allowed to access this view
    permission_required = ('administrator')

    # check if the form is valid or not after submitting it
    def post(self, request, *args, **kwargs):
        form = BusinessTypeForm(request.POST)
        if self.form_valid(form):
            print("valid")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
        return super().get(request)

    def form_valid(self, form):
        # return added  business_name
        business_name = self.request.POST['name']
        # save form data if form is valid
        form.save()
        # present success message to the user
        messages.success(self.request, f"Business {business_name} Added Successfully")
        # return the control to the original overridden function in the super class
        return super().form_valid(form)

    # priovided the required extra context for the view
    extra_context = {
        'masters': 'active',
        'business_types': 'active',
        'title': 'Add Business Type'
    }


"""
BusinessTypeListView:
This class is used to view all added business types in the system,
it allows only administrators and monitor users to  
access.
"""
class BusinessListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = BusnessType
    # specify the template in the view
    template_name = "business_type/business_type_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = "Business Type"
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'masters': 'active',
        'business_types': 'active',
        'no_records_admin': NO_RECORDS_FOR_BUSINESS_TYPE_MODEL_ADMIN_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_BUSINESS_TYPE_MODEL_MONITOR_MESSAGE
    }
    searchManObj = SearchMan("Business_Type")
 
    # return default queryset used in this view
    def get_queryset(self):
        return BusnessType.objects.all().order_by('-id')

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
            states = BusnessType.objects.all().order_by('-id')
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
            'object_list': BusinessTypeForm,
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
Agent Shift FormView:
This class is used to represent the add agent shifts view , 
it allows only ouloug_admin users to access it
"""


class AgentShiftFormView(OulougGroupPermission, FormView):
    # specify template name used to add new business_type
    template_name = 'agent_shift/add_agent_shifts.html'
    # specify the form used
    form_class = AgentShiftForm
    # specify the page to return to after successfully adding new currency
    success_url = 'agentShifts'
    # specify user's groups allowed to access this view
    permission_required = ('administrator')

    # check if the form is valid or not after submitting it
    def post(self, request, *args, **kwargs):
        form = BusinessTypeForm(request.POST)
        if self.form_valid(form):
            print("valid")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
        return super().get(request)

    def form_valid(self, form):
        # return added  business_name
        shift_name = self.request.POST['name']
        # save form data if form is valid
        form.save()
        # present success message to the user
        messages.success(self.request, f"Shift {shift_name} Added Successfully")
        # return the control to the original overridden function in the super class
        return super().form_valid(form)

    # priovided the required extra context for the view
    extra_context = {
        'ouloug_services': 'active',
        'agent_shifts': 'active',
        'title': 'Add Agent Shifts'
    }


"""
AgentShiftListView:
This class is used to view all added agent shifts in the system,
it allows only administrators and monitor users to  
access.
"""


class AgentShiftListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = AgentShift
    # specify the template in the view
    template_name = "agent_shift/agent_shift_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = "Agent Shifts"
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'ouloug_Services': 'active',
        'agent_shifts': 'active',
        'no_records_admin': NO_RECORDS_FOR_AGENT_SHIFT_MODEL_ADMIN_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_AGENT_SHIFT_MODEL_MONITOR_MESSAGE
    }
    searchManObj = SearchMan("AgentShift")

    # return default queryset used in this view
    def get_queryset(self):
        return AgentShift.objects.all().order_by('-id')

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
            agentShifts = AgentShift.objects.all().order_by('-id')
            self.searchManObj.setPaginator(agentShifts)
            self.searchManObj.setSearch(False)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
            agentShifts = paginator.page(page)
            # Create a page object for the current page.
        except PageNotAnInteger:
            # If the query parameter is empty then grab the first page.
            agentShifts = paginator.page(1)
            page = 1
        except EmptyPage:
            # If the query parameter is greater than num_pages then grab the last page.
            agentShifts = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        self.extra_context.update({
            'ouloug_services': 'active',
            'page_range': paginator.page_range,
            'num_pages': paginator.num_pages,
            'object_list': BusinessTypeForm,
            # 'search': self.searchManObj.getSearch(),
            # 'search_result': self.search_result,
            # 'search_phrase': self.searchManObj.getSearchPhrase(),
            # 'search_option': self.searchManObj.getSearchOption(),
            # 'search_error': self.searchManObj.getSearchError(),
            'current_page': page,
            'title': self.title
        })
        return super().get(request)

