from django.shortcuts import render
from django.shortcuts import redirect

from Util.utils import SearchMan, OulougGroupPermission
from .models import Service
from django.views.generic import ListView, FormView
from .forms import ServiceForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import PermissionRequiredMixin
from Util.static_strings import (NO_RECORDS_FOR_SERVICE_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_SERVICE_MODEL_ADMIN_MESSAGE, NO_RECORDS_FOR_CITY_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_CITY_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_STATE_MODEL_ADMIN_MESSAGE,
                                 NO_RECORDS_FOR_STATE_MODEL_MONITOR_MESSAGE
                                 )
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
"""
ServiceListView:
This class is used to view all added services in the system,
it allows only administrators and monitor users to  
access.
"""


class ServiceListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = Service
    # specify the template in the view
    template_name = "service/services_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = "Services"
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'ouloug_services': 'active',
        'services': 'active',
        'no_records_admin': NO_RECORDS_FOR_SERVICE_MODEL_ADMIN_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_SERVICE_MODEL_MONITOR_MESSAGE
    }
    searchManObj = SearchMan("Service")

    # return default queryset used in this view
    def get_queryset(self):
        return Service.objects.all().order_by('-id')

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
            services = Service.objects.all().order_by('-id')
            self.searchManObj.setPaginator(services)
            self.searchManObj.setSearch(False)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
            services = paginator.page(page)
            # Create a page object for the current page.
        except PageNotAnInteger:
            # If the query parameter is empty then grab the first page.
            services = paginator.page(1)
            page = 1
        except EmptyPage:
            # If the query parameter is greater than num_pages then grab the last page.
            services = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        self.extra_context.update({
            'ouloug_services': 'active',
            'page_range': paginator.page_range,
            'num_pages': paginator.num_pages,
            'object_list': services,
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
ServiceFormView:
This class is used to represent the add service view , 
it allows only ouloug_admin users to access it
"""


class ServiceFormView(OulougGroupPermission, FormView):
    # specify template name used to add new countries
    template_name = 'service/add_services.html'
    # specify the form used
    form_class = ServiceForm
    # specify the page to return to after successfully adding new country
    success_url = 'services'
    # specify user's groups allowed to access this view
    permission_required = ('administrator')

    # check if the form is valid or not after submitting it
    def post(self, request, *args, **kwargs):
        form = ServiceForm(request.POST)
        if self.form_valid(form):
            print("valid")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
        return super().get(request)

    def form_valid(self, form):
        # return added country name
        service_name = self.request.POST['name']
        # save form data if form is valid
        try:
            form.save()
            # present success message to the user
            messages.success(self.request, f"Service <<{service_name}>> Added Successfully")
        except:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(self.request, '{}: {}'.format(field, item))

        # return the control to the original overridden function in the super class
        return super().form_valid(form)

    # providing the required extra context for the view
    extra_context = {
        'ouloug_services': 'active',
        'services': 'active',
        'title': _('Add Services')
    }
