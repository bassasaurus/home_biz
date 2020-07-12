from django.shortcuts import render
from django.contrib.auth.views import (
                LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
                PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView,
                PasswordResetView)

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginRequired(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class LoginView(LoginView):

    form_class = AuthenticationForm
    template_name = 'registration/login.html'


class LogoutView(LogoutView):

    template_name = 'registration/logged_out.html'
