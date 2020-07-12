
from django.views.generic import TemplateView
from authentication.views import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'common/home.html'
