from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Util.utils import SearchMan
from Util.static_strings import (
    SEARCH_STATES_TIP, CLEAR_SEARCH_TIP
)
from apps.common_views.views import BaseListView
from apps.common_views.useful_functions import get_filtered_query


class TelecomsListView(BaseListView):
    searchManObj = None
    search_result = ''
    is_search_ordered = False
    order_field = ''
    ordering_value = "Ascending"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.searchManObj = SearchMan(self.model_name)

    def get(self, request, *args, **kwargs):
        from apps.telecoms.models import TelecomOperator
        from Util.lists_of_data import TELECOM_STATUS
        # self.searchManObj.set_querySet(self.get_queryset())
        queryset = self.searchManObj.get_queryset()
        paginator = Paginator(queryset, 5)
        if 'filter_value' in request.GET and 'clear' not in request.GET:
            field_name = self.request.GET['filter_by']
            field_value = self.request.GET['filter_value']
            if field_name == 'none':
                messages.error(request,
                               "Please choose field to search by first!")
                self.searchManObj.setSearchError(True)
            else:
                if field_name == "status":
                    field_value = self.request.GET['filter_value']
                    self.search_result = TelecomOperator.objects.filter(
                        status=field_value).order_by('id')
                    ordering = self.request.GET['filter_ordering']
                    order_by_filed = self.request.GET['order_by']
                    filtered_object = get_filtered_query(False, 'equal', field_name, field_value)
                    if order_by_filed and order_by_filed != 'none':
                        self.is_search_ordered = True
                        self.order_field = order_by_filed
                        if ordering == "asc":
                            self.search_result = TelecomOperator.objects.filter(filtered_object).order_by(
                                order_by_filed)
                            self.ordering_value = "Ascending"
                        else:
                            order_by_filed = '-' + order_by_filed
                            self.search_result = TelecomOperator.objects.filter(filtered_object).order_by(
                                order_by_filed)
                            self.ordering_value = "Descending"
                    else:
                        self.is_search_ordered = False
                        self.search_result = TelecomOperator.objects.filter(filtered_object)
                    self.searchManObj.setPaginator(self.search_result)
                    self.searchManObj.setSearchPhrase(field_value)
                    self.searchManObj.setSearchOption('Status')
                    self.searchManObj.setSearchError(False)
                    self.searchManObj.set_querySet(self.search_result)
                    self.searchManObj.setSearch(True)
        if 'page' not in request.GET and 'filter_by' not in request.GET:
            instances = self.model.objects.all().order_by('-id')
            self.searchManObj.setPaginator(instances)
            self.searchManObj.setSearch(False)
            self.searchManObj.set_querySet(instances)
        if 'clear' in request.GET:
            instances = self.model.objects.all().order_by('-id')
            self.searchManObj.setPaginator(instances)
            self.searchManObj.setSearch(False)
            self.searchManObj.set_querySet(instances)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
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
            "instances_count": len(self.searchManObj.get_queryset()),
            "is_search_ordered": self.is_search_ordered,
            "order_by_field": self.order_field,
            "ordering_value": self.ordering_value,
            'search': self.searchManObj.getSearch(),
            'search_result': self.search_result,
            'search_phrase': self.searchManObj.getSearchPhrase(),
            'search_option': self.searchManObj.getSearchOption(),
            'search_error': self.searchManObj.getSearchError(),
            'current_page': page,
            'search_states_tip': SEARCH_STATES_TIP,
            'clear_search_tip': CLEAR_SEARCH_TIP,
            'title': self.title,
            'data_js': {
                "status": TELECOM_STATUS,
            }
        }
        return super().get(request)

class TelecomNumbersListView(BaseListView):
    searchManObj = None
    search_result = ''
    is_search_ordered = False
    order_field = ''
    ordering_value = "Ascending"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.searchManObj = SearchMan(self.model_name)

    def get(self, request, *args, **kwargs):
        from apps.telecoms.models import TelecomNumber,TelecomOperator
        from Util.lists_of_data import TELECOM_NUMBER_STATUS,TELECOM_NUMBER_TYPE
        queryset = self.searchManObj.get_queryset()
        paginator = Paginator(queryset, 5)
        if 'filter_value' in request.GET and 'clear' not in request.GET:
            field_name = self.request.GET['filter_by']
            field_value = self.request.GET['filter_value']
            if field_name == 'none':
                messages.error(request,
                               "Please choose field to search by first!")
                self.searchManObj.setSearchError(True)
            else:
                if field_name == "status":
                    field_value = self.request.GET['filter_value']
                    self.search_result = TelecomNumber.objects.filter(
                        status=field_value).order_by('id')
                    ordering = self.request.GET['filter_ordering']
                    order_by_filed = self.request.GET['order_by']
                    filtered_object = get_filtered_query(False, 'equal', field_name, field_value)
                    if order_by_filed and order_by_filed != 'none':
                        self.is_search_ordered = True
                        self.order_field = order_by_filed
                        if ordering == "asc":
                            self.search_result = TelecomNumber.objects.filter(filtered_object).order_by(
                                order_by_filed)
                            self.ordering_value = "Ascending"
                        else:
                            order_by_filed = '-' + order_by_filed
                            self.search_result = TelecomNumber.objects.filter(filtered_object).order_by(
                                order_by_filed)
                            self.ordering_value = "Descending"
                    else:
                        self.is_search_ordered = False
                        self.search_result = TelecomNumber.objects.filter(filtered_object)
                    self.searchManObj.setPaginator(self.search_result)
                    self.searchManObj.setSearchPhrase(field_value)
                    self.searchManObj.setSearchOption('Status')
                    self.searchManObj.setSearchError(False)
                    self.searchManObj.set_querySet(self.search_result)
                    self.searchManObj.setSearch(True)

                if field_name == "telecom":
                    field_value = self.request.GET['filter_value']
                    self.search_result = TelecomNumber.objects.filter(
                    telecom__name=field_value).order_by('id')
                    ordering = self.request.GET['filter_ordering']
                    order_by_filed = self.request.GET['order_by']
                    filtered_object = get_filtered_query(True,"contains",field_name,field_value,'name')
                    if order_by_filed and order_by_filed != 'none':
                        self.is_search_ordered = True
                        self.order_field = order_by_filed
                        if ordering == "asc":
                            self.search_result = TelecomNumber.objects.filter(filtered_object).order_by(
                            order_by_filed)
                            self.ordering_value = "Ascending"
                        else:
                            order_by_filed = '-' + order_by_filed
                            self.search_result = TelecomNumber.objects.filter(filtered_object).order_by(
                            order_by_filed)
                            self.ordering_value = "Descending"
                    else:
                        self.is_search_ordered = False
                        self.search_result = TelecomNumber.objects.filter(filtered_object)
                    self.searchManObj.setPaginator(self.search_result)
                    self.searchManObj.setSearchPhrase(field_value)
                    self.searchManObj.setSearchOption('Telecom')
                    self.searchManObj.setSearchError(False)
                    self.searchManObj.set_querySet(self.search_result)
                    self.searchManObj.setSearch(True)

                if field_name == "type":
                    field_value = self.request.GET['filter_value']
                    self.search_result = TelecomNumber.objects.filter(
                    type=field_value).order_by('id')
                    ordering = self.request.GET['filter_ordering']
                    order_by_filed = self.request.GET['order_by']
                    filtered_object = get_filtered_query(False,"equal",field_name,field_value)
                    if order_by_filed and order_by_filed != 'none':
                        self.is_search_ordered = True
                        self.order_field = order_by_filed
                        if ordering == "asc":
                            self.search_result = TelecomNumber.objects.filter(filtered_object).order_by(
                            order_by_filed)
                            self.ordering_value = "Ascending"
                        else:
                            order_by_filed = '-' + order_by_filed
                            self.search_result = TelecomNumber.objects.filter(filtered_object).order_by(
                            order_by_filed)
                            self.ordering_value = "Descending"
                    else:
                        self.is_search_ordered = False
                        self.search_result = TelecomNumber.objects.filter(filtered_object)
                    self.searchManObj.setPaginator(self.search_result)
                    self.searchManObj.setSearchPhrase(field_value)
                    self.searchManObj.setSearchOption('Type')
                    self.searchManObj.setSearchError(False)
                    self.searchManObj.set_querySet(self.search_result)
                    self.searchManObj.setSearch(True)
        if 'page' not in request.GET and 'filter_by' not in request.GET:
            instances = self.model.objects.all().order_by('-id')
            self.searchManObj.setPaginator(instances)
            self.searchManObj.setSearch(False)
            self.searchManObj.set_querySet(instances)
        if 'clear' in request.GET:
            instances = self.model.objects.all().order_by('-id')
            self.searchManObj.setPaginator(instances)
            self.searchManObj.setSearch(False)
            self.searchManObj.set_querySet(instances)
        if request.GET.get('page'):
            # Grab the current page from query parameter consultant
            page = int(request.GET.get('page'))
        else:
            page = None

        try:
            paginator = self.searchManObj.getPaginator()
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
            "instances_count": len(self.searchManObj.get_queryset()),
            "is_search_ordered": self.is_search_ordered,
            "order_by_field": self.order_field,
            "ordering_value": self.ordering_value,
            'search': self.searchManObj.getSearch(),
            'search_result': self.search_result,
            'search_phrase': self.searchManObj.getSearchPhrase(),
            'search_option': self.searchManObj.getSearchOption(),
            'search_error': self.searchManObj.getSearchError(),
            'current_page': page,
            'search_states_tip': SEARCH_STATES_TIP,
            'clear_search_tip': CLEAR_SEARCH_TIP,
            'title': self.title,
            'data_js': {
                "status": TELECOM_NUMBER_STATUS,
                "type": TELECOM_NUMBER_TYPE,
                "telecoms_list": list(TelecomOperator.objects.values('name')),
            }
        }
        return super().get(request)