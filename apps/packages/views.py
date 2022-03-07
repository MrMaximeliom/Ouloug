from django.shortcuts import get_object_or_404, redirect

from Util.utils import SearchMan
from .models import Package
from django.views.generic import ListView, FormView
from .forms import PackageForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from Util.static_strings import (NO_RECORDS_FOR_PACKAGE_MODEL_MONITOR_MESSAGE,
                                 NO_RECORDS_FOR_PACKAGE_MODEL_ADMIN_MESSAGE,
                                 )
from Util.utils import OulougGroupPermission
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

"""
PackageListView:
This class is used to view all added packages in the system,
it allows only administrators and monitor users to  
access.
"""
class PackageListView(OulougGroupPermission, ListView):
    # specify the model used in the view
    model = Package
    # specify the template in the view
    template_name = "package/packages_list.html"
    # adding active flag for the sidebar active link

    # adding the view's title
    title = "Packages"
    permission_denied_message = _("Sorry you do not have access to this page")
    # adding the required extra context
    extra_context = {
        'title': title,
        'ouloug_services': 'active',
        'packages': 'active',
        'no_records_admin': NO_RECORDS_FOR_PACKAGE_MODEL_ADMIN_MESSAGE,
        'no_records_monitor': NO_RECORDS_FOR_PACKAGE_MODEL_MONITOR_MESSAGE
    }
    searchManObj = SearchMan("Package")

    # return default queryset used in this view
    def get_queryset(self):
        return Package.objects.all().order_by('-id')

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
            packages = Package.objects.all().order_by('-id')
            self.searchManObj.setPaginator(packages)
            self.searchManObj.setSearch(False)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
            packages = paginator.page(page)
            # Create a page object for the current page.
        except PageNotAnInteger:
            # If the query parameter is empty then grab the first page.
            packages = paginator.page(1)
            page = 1
        except EmptyPage:
            # If the query parameter is greater than num_pages then grab the last page.
            packages = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        self.extra_context.update({
            'page_range': paginator.page_range,
            'num_pages': paginator.num_pages,
            'object_list': packages,
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
PackageFormView:
This class is used to represent the add package view , 
it allows only ouloug_admin users to access it
"""
class PackageFormView(OulougGroupPermission, FormView):
    # specify template name used to add new countries
    template_name = 'package/add_packages.html'
    # specify the form used
    form_class = PackageForm
    # specify the page to return to after successfully adding new country
    success_url = 'packages'
    # specify user's groups allowed to access this view
    permission_required = ('administrator')

    # check if the form is valid or not after submitting it
    def post(self, request, *args, **kwargs):
        form = PackageForm(request.POST)
        if self.form_valid(form):
            print("valid")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
        return super().get(request)

    def form_valid(self, form):
        # return added country name
        package_name = self.request.POST['name']
        # save form data if form is valid
        form.save()
        # present success message to the user
        messages.success(self.request, f"Package<<{package_name}>> Added Successfully")
        # return the control to the original overridden function in the super class
        return super().form_valid(form)

    # priovided the required extra context for the view
    extra_context = {
        'ouloug_services': 'active',
        'packages': 'active',
        'add_packages': 'active',
        'title': 'Add Packages'
    }
"""
Change Package Status:
this method is used to change the status of the package 
"""
def changePackageStatus(request,pk,status):
    package = get_object_or_404(Package, pk=pk)
    if status == False:
        package.status = True
    else:
        package.status = False
    package.save()
    messages.success(request,f"package <<{package.name}>> updated successfully")
    return redirect('packagesList')

