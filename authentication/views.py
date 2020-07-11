from django.shortcuts import render
from django.contrib.auth.views import (
                LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
                PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView,
                PasswordResetView)

from django.contrib.auth.forms import AuthenticationForm


class LoginView(LoginView):

    form_class = AuthenticationForm
    template_name = 'registration/login.html'


class LogoutView(LogoutView):

    template_name = 'registration/logged_out.html'
