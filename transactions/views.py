from authentication.views import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from transactions.models import Transactions, BusinessGroups, Accounts, Categories
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from transactions.forms import TransactionsForm


class TransactionsListView(LoginRequiredMixin, ListView):
    model = Transactions
    template_name = 'transactions/transactions_list.html'


class TransactionsCreateView(LoginRequiredMixin, CreateView):
    model = Transactions
    template_name = 'transactions/transactions_create.html'
    success_url = reverse_lazy('transactions_list')
    form_class = TransactionsForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TransactionsCreateView, self).form_valid(form)


class TransactionsDetailView(LoginRequiredMixin, DetailView):
    model = Transactions
    template_name = 'transactions/transactions_detail.html'


class TransactionsUpdateView(LoginRequiredMixin, UpdateView):
    model = Transactions
    fields = ['name', 'amount', 'categories', 'categories', 'business_groups', 'comments']
    template_name = 'transactions/transactions_update.html'

    def get_success_url(self):
        return reverse('transactions_detail', kwargs={'pk': self.object.pk})

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
    success_url = reverse_lazy('business_list')

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

    def get_success_url(self):
        return reverse('business_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super(BusinessGroupsUpdateView, self).form_valid(form)


class BusinessGroupsDeleteView(LoginRequiredMixin, DeleteView):
    model = BusinessGroups
    template_name = 'business_groups/business_groups_delete.html'
    success_url = reverse_lazy('business_list')


class AccountsListView(LoginRequiredMixin, ListView):
    model = Accounts
    template_name = 'accounts/accounts_list.html'


class AccountsCreateView(LoginRequiredMixin, CreateView):
    model = Accounts
    fields = ['name', 'balance']
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
    fields = ['name', 'balance']
    template_name = 'accounts/accounts_update.html'

    def get_success_url(self):
        return reverse('accounts_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super(AccountsUpdateView, self).form_valid(form)


class AccountsDeleteView(LoginRequiredMixin, DeleteView):
    model = Accounts
    template_name = 'accounts/accounts_delete.html'
    success_url = reverse_lazy('accounts_list')


class CategoriesListView(LoginRequiredMixin, ListView):
    model = Categories
    template_name = 'categories/categories_list.html'


class CategoriesCreateView(LoginRequiredMixin, CreateView):
    model = Categories
    fields = ['name', 'amount']
    template_name = 'categories/categories_create.html'
    success_url = reverse_lazy('categories_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CategoriesCreateView, self).form_valid(form)


class CategoriesDetailView(LoginRequiredMixin, DetailView):
    model = Categories
    template_name = 'categories/categories_detail.html'


class CategoriesUpdateView(LoginRequiredMixin, UpdateView):
    model = Categories
    fields = ['name', 'amount']
    template_name = 'categories/categories_update.html'

    def get_success_url(self):
        return reverse('categories_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super(CategoriesUpdateView, self).form_valid(form)


class CategoriesDeleteView(LoginRequiredMixin, DeleteView):
    model = Categories
    template_name = 'categories/categories_delete.html'
    success_url = reverse_lazy('categories_list')
