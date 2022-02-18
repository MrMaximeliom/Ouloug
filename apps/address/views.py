from .models import Country
from django.views.generic import ListView,FormView
from .forms import CountryForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.mixins import PermissionRequiredMixin
# from Util.GroupPermissions import GroupRequiredMixin
class VoteListView(PermissionRequiredMixin, ListView):
  permission_required = 'school.add_vote'
  # Or multiple of permissions<br>permission_required = ('school .add_vote', 'school .change_vote'

class CountryFormView(FormView):
    template_name = 'countries/add_countries.html'
    form_class = CountryForm
    success_url = 'countries'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Offer Added Successfully")
        return super().form_valid(form)

    extra_context = {
        'masters': 'active',
        'countries': 'active',
        'add_offers': 'active',
        'title':'Add Countries'
    }
# Create your views here.
class CountryListView(PermissionRequiredMixin,ListView):
    model = Country
    template_name = "countries/countries_list.html"
    active_flag = 'all_offers'
    title = "Countries"
    permission_denied_message = _("Sorry you do not have access to this page")
    permission_required = ('ouloug_admin','ouloug_monitor')
    def has_permission(self):
        groups = self.get_permission_required()
        user_groups = self.request.user.groups.values('name')
        for group in groups:
            for user_group in user_groups:
                if user_group['name'] == group:
                    return True

    extra_context = {
        'title':title,
        'masters':'active',
        'countries':'active'
    }



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

    # def get(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     paginator = Paginator(queryset, 5)
    #     if 'temp_dir' in request.session:
    #         # deleting temp dir in GET requests
    #         if request.session['temp_dir'] != '':
    #             delete_temp_folder()
    #     if 'page' not in request.GET:
    #         offers = Offer.objects.all().order_by('-id')
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
    #
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
    #         'not_found':OFFER_NOT_FOUND,
    #         'current_page': page,
    #         'title': self.title
    #     }
    #     return super().get(request)