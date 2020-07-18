from django.views.generic import TemplateView
from authentication.views import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from transactions.models import Transactions, BusinessGroups, Accounts
from django.urls import reverse_lazy, reverse


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'common/home.html'


class IndexView(TemplateView):
    template_name = 'common/index.html'


class TransactionsListView(LoginRequiredMixin, ListView):
    model = Transactions
    template_name = 'transactions/transactions_list.html'


class TransactionsCreateView(LoginRequiredMixin, CreateView):
    model = Transactions
    fields = ['name', 'date', 'amount', 'accounts', 'categories', 'business_groups', 'comments']
    template_name = 'transactions/transactions_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TransactionsCreateView, self).form_valid(form)


class TransactionsDetailView(LoginRequiredMixin, DetailView):
    model = Transactions
    template_name = 'transactions/transactions_detail.html'


class TransactionsUpdateView(LoginRequiredMixin, UpdateView):
    model = Transactions
    fields = ['name', 'amount', 'accounts', 'categories', 'business_groups', 'comments']
    template_name = 'transactions/transactions_update.html'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super(TransactionsUpdateView, self).form_valid(form)


class TransactionsDeleteView(LoginRequiredMixin, DeleteView):
    model = Transactions
    template_name = 'transactions/transactions_delete.html'
    success_url = reverse_lazy('transactions_list')


class BusinessGroupsListView(LoginRequiredMixin, ListView):
    model = BusinessGroups
    template_name = 'business_groups/business_groups_list.html'


class BusinessGroupsCreateView(LoginRequiredMixin, CreateView):
    model = BusinessGroups
    fields = ['name', ]
    template_name = 'business_groups/business_groups_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(BusinessGroupsCreateView, self).form_valid(form)


class BusinessGroupsDetailView(LoginRequiredMixin, DetailView):
    model = BusinessGroups
    template_name = 'business_groups/business_groups_detail.html'


class BusinessGroupsUpdateView(LoginRequiredMixin, UpdateView):
    model = BusinessGroups
    fields = ['name', ]
    template_name = 'business_groups/business_groups_update.html'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super(BusinessGroupsUpdateView, self).form_valid(form)


class BusinessGroupsDeleteView(LoginRequiredMixin, DeleteView):
    model = BusinessGroups
    template_name = 'business_groups/business_groups_delete.html'
    success_url = reverse_lazy('business_groups_list')


class AccountsListView(LoginRequiredMixin, ListView):
    model = Accounts
    template_name = 'accounts/accounts_list.html'


class AccountsCreateView(LoginRequiredMixin, CreateView):
    model = Accounts
    fields = ['name', ]
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('accounts_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(AccountsCreateView, self).form_valid(form)


class AccountsDetailView(LoginRequiredMixin, DetailView):
    model = Accounts
    template_name = 'accounts/accounts_detail.html'


class AccountsUpdateView(LoginRequiredMixin, UpdateView):
    model = Accounts
    fields = ['name', ]
    template_name = 'accounts/accounts_update.html'

    def get_success_url(self):
        return reverse('accounts-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super(AccountsUpdateView, self).form_valid(form)


class AccountsDeleteView(LoginRequiredMixin, DeleteView):
    model = Accounts
    template_name = 'accounts/accounts_delete.html'
    success_url = reverse_lazy('accounts_list')
