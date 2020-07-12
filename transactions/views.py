
from django.views.generic import TemplateView
from authentication.views import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from BusinessGroups.models import Transactions, BusinessGroups, Accounts
from django.urls import reverse_lazy


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'common/home.html'


class TransactionsListView(ListView):
    model = Transactions
    template_name = 'transactions/transactions_list.html'


class TransactionsCreateView(CreateView):
    model = Transactions
    fields = ['name', 'amount', 'accounts', 'categories', 'business_groups', 'comments']
    template_name = 'transactions/transactions_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TransactionsCreateView, self).form_valid(form)


class TransactionsDetailView(DetailView):
    model = Transactions
    template_name = 'transactions/transactions_detail.html'


class TransactionsUpdateView(UpdateView):
    model = Transactions
    fields = ['name', 'amount', 'accounts', 'categories', 'business_groups', 'comments']
    template_name = 'transactions/transactions_update.html'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super(TransactionsUpdateView, self).form_valid(form)


class TransactionsDeleteView(DeleteView):
    model = Transactions
    template_name = 'transactions/transactions_delete.html'
    success_url = reverse_lazy('transactions_list')



class BusinessGroupsListView(ListView):
    model = BusinessGroups
    template_name = 'business_groups/business_groups_list.html'


class BusinessGroupsCreateView(CreateView):
    model = BusinessGroups
    fields = ['name', 'amount', 'accounts', 'categories', 'business_groups', 'comments']
    template_name = 'business_groups/business_groups_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(BusinessGroupsCreateView, self).form_valid(form)


class BusinessGroupsDetailView(DetailView):
    model = BusinessGroups
    template_name = 'business_groups/business_groups_detail.html'


class BusinessGroupsUpdateView(UpdateView):
    model = BusinessGroups
    fields = ['name', 'amount', 'accounts', 'categories', 'business_groups', 'comments']
    template_name = 'business_groups/business_groups_update.html'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super(BusinessGroupsUpdateView, self).form_valid(form)


class BusinessGroupsDeleteView(DeleteView):
    model = BusinessGroups
    template_name = 'business_groups/business_groups_delete.html'
    success_url = reverse_lazy('business_groups_list')
