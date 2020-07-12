
from django.views.generic import TemplateView
from authentication.views import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'common/home.html'


class TransactionsListView(ListView):
    template_name = 'transactions_list.html'


class TransactionsCreateView(CreateView):
    template_name = 'transactions_create.html'


class TransactionsDetailView(DetailView):
    template_name = 'transactions_detail.html'


class TransactionsUpdateView(DetailView):
    template_name = 'transactions_update.html'


class TransactionsDeleteView(DeleteView):
    template_name = 'transactions_delete.html'
