from django.urls import path, include
from authenication.views import LoginView, LogoutView


urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_View(), name='logout')
]
