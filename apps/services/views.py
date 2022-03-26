from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib import messages
from Util.utils import SearchMan
<<<<<<< HEAD
                                 
=======


>>>>>>> 3750bedeabae27a9145c87fe7665ebe2af3be414
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.generic.edit import UpdateView

<<<<<<< HEAD
from models import Service

=======
>>>>>>> 3750bedeabae27a9145c87fe7665ebe2af3be414
# Create your views here.
from .models import Service

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
            self.main_active_flag: "active",
            self.active_flag: "active"
        }
        return super(AddModelView, self).get(self)

    def post(self, request, *args, **kwargs):
        self.extra_context = {
            self.main_active_flag: "active",
            self.active_flag: "active"
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

    # providing the required extra context for the view
    extra_context = {
        'ouloug_services': 'active',
        'services': 'active',
        'title': 'Add Services'
    }
def changeServiceStatus(request,pk,status):
    service = get_object_or_404(Service, pk=pk)
    if status == 'active':
        service.status = 'active'
    elif status == 'not_active':
        service.status = 'not_active'
    service.save()
    messages.success(request,f"service <<{service.name}>> updated successfully")
    return redirect('servicesList')


# This's for service update 
<<<<<<< HEAD
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
        
=======



>>>>>>> 3750bedeabae27a9145c87fe7665ebe2af3be414
