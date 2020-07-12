
from django.views.generic import TemplateView
from authentication.views import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from transactions.models import Transactions


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'common/home.html'


class TransactionsListView(ListView):
    model = Transactions
    template_name = 'transactions/transactions_list.html'


class TransactionsCreateView(CreateView):
    model = Transactions
    template_name = 'transactions/transactions_create.html'


class TransactionsDetailView(DetailView):
    model = Transactions
    template_name = 'transactions/transactions_detail.html'


class TransactionsUpdateView(DetailView):
    model = Transactions
    template_name = 'transactions/transactions_update.html'


class TransactionsDeleteView(DeleteView):
    model = Transactions
    template_name = 'transactions/transactions_delete.html'
