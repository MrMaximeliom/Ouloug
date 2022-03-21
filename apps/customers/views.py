from Util.utils import SearchMan
from apps.customers.forms import BusinessTypeForm,AgentShiftForm
from .models import BusinessType,AgentShift,CustomerCall
from django.views.generic import ListView, FormView,CreateView,UpdateView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from Util.static_strings import (
                                 NO_RECORDS_FOR_BUSINESS_TYPE_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_BUSINESS_TYPE_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_AGENT_SHIFT_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_AGENT_SHIFT_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_CUSTOMER_CALL_MODEL_MESSAGE

                                 )
from Util.utils import OulougGroupPermission
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage





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
    model = BusinessType
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
        return BusinessType.objects.all().order_by('-id')

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
            states = BusinessType.objects.all().order_by('-id')
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




"""
CustomerCallListView:
This class is used to view all added customer calls in the system,
it allows only administrators and monitor users to  
access.
"""
class CustomerCallListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = CustomerCall
    # specify the template in the view
    template_name = "customer_call/customer_call_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = "Customer Calls"
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'customers': 'active',
        'customer_call': 'active',
        'no_records_admin': NO_RECORDS_FOR_CUSTOMER_CALL_MODEL_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_CUSTOMER_CALL_MODEL_MESSAGE
    }
    searchManObj = SearchMan("CustomerCall")

    # return default queryset used in this view
    def get_queryset(self):
        return CustomerCall.objects.all().order_by('-id')

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
            customerCalls = CustomerCall.objects.all().order_by('-id')
            self.searchManObj.setPaginator(customerCalls)
            self.searchManObj.setSearch(False)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
            customerCalls = paginator.page(page)
            # Create a page object for the current page.
        except PageNotAnInteger:
            # If the query parameter is empty then grab the first page.
            customerCalls = paginator.page(1)
            page = 1
        except EmptyPage:
            # If the query parameter is greater than num_pages then grab the last page.
            customerCalls = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        self.extra_context.update({

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
ModelListView Class:
is a class used to list instances of a specified model,
it requires to define the following params:
- model (the model of the updated instance)
- template_name ( the path of the view that will be used)
- active_flag (this flag is used to add 'active' class to the current pages in sidebar) 
- main_active_flag (this flag is used to add 'active' class to the main master current pages in sidebar) 
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
    main_active_flag = None
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
            self.main_active_flag: 'active',
            self.active_flag: "active",
            "no_records_admin": self.no_records_admin,
            "no_records_monitor": self.no_records_monitor,
            "add_tool_tip_text": self.add_tool_tip_text,
            "update_tool_tip_text": self.update_tool_tip_text,
            "instances_count": len(self.get_queryset()),

            # 'search': self.searchManObj.getSearch(),
            # 'search_result': self.search_result,
            # 'search_phrase': self.searchManObj.getSearchPhrase(),
            # 'search_option': self.searchManObj.getSearchOption(),
            # 'search_error': self.searchManObj.getSearchError(),
            'current_page': page,
        }
        return super().get(request)

"""
AddModelView Class:
is a class used to add instances of a specified model,
it requires to define the following params:
- model (the model to add new instances)
- template_name ( the path of the view that will be used)
- active_flag (this flag is used to add 'active' class to the current pages in sidebar) 
- reference_field_name (this field used to reference the field that will be used in success/error messages) 
- main_active_flag (this flag is used to add 'active' class to the main master current pages in sidebar)
"""


class AddModelView(CreateView):
    model = None
    fields = None
    template_name = None
    active_flag = None
    reference_field_name = None
    main_active_flag = None

    def form_invalid(self, form):
        for field, items in form.errors.items():
            for item in items:
                print('{}: {}'.format(field, item))
        instance_name = form.cleaned_data[self.reference_field_name]
        messages.error(self.request, f"{self.active_flag} <<{instance_name}>> did not added , please try again!")
        return super(AddModelView, self).form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        instance_name = form.cleaned_data[self.reference_field_name]
        self.object.added_by = self.request.user
        self.object.save()
        messages.success(self.request, f"{self.active_flag} <<{instance_name}>> added successfully")
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.extra_context = {
            self.main_active_flag:"active",
            self.active_flag: "active"
        }
        return super(AddModelView, self).get(self)

    def post(self, request, *args, **kwargs):
        self.extra_context = {
            self.main_active_flag:"active",
            self.active_flag:"active"
        }
        return super(AddModelView, self).post(self)



"""
UpdateModelView Class:
is a class used to update instances of a specified model,
it requires to define the following params:
- model (the model of the updated instance)
- template_name ( the path of the view that will be used)
- active_flag (this flag is used to add 'active' class to the current pages in sidebar) 
- reference_field_name (this field used to reference the field that will be used in success/error messages) 
- main_active_flag (this flag is used to add 'active' class to the main master current pages in sidebar)

"""


class UpdateModelView(UpdateView):
    model = None
    fields = None
    template_name = None
    active_flag = None
    reference_field_name = None
    main_active_flag = None


    def form_invalid(self, form):
        for field, items in form.errors.items():
            for item in items:
                print('{}: {}'.format(field, item))
        instance_name = form.cleaned_data[self.reference_field_name]
        messages.error(self.request, f"{self.active_flag} <<{instance_name}>> did not updated , please try again!")
        return super(UpdateModelView, self).form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.last_modified_by = self.request.user
        self.object.save()
        instance_name = form.cleaned_data[self.reference_field_name]
        messages.success(self.request, f"{self.active_flag} <<{instance_name}>> updated successfully")
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.extra_context = {
            self.main_active_flag:"active",
            self.active_flag: "active"
        }
        return super(UpdateModelView, self).get(self)

    def post(self, request, *args, **kwargs):
        self.extra_context = {
            self.main_active_flag:"active",
            self.active_flag: "active"
        }
        return super(UpdateModelView, self).post(self)
