from django.urls import path
from transactions.views import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]
