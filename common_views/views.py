from django.views.generic import TemplateView
from django.shortcuts import redirect
from authentication.views import LoginRequiredMixin
from transactions.models import Transactions, BusinessGroups, Accounts, Categories


class IndexView(TemplateView):
    template_name = 'common/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return super(IndexView, self).dispatch(request, *args, **kwargs)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transactions.objects.all()
        context['businesses'] = BusinessGroups.objects.all()
        context['accounts'] = Accounts.objects.all()
        context['categories'] = Categories.objects.all()
        return context
