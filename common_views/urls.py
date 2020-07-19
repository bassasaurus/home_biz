from django.urls import path
from common_views.views import IndexView, HomeView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home')
]
