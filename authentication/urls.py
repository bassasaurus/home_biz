from django.urls import path, include
from authenication.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_View(), name='logout',
    # path('accounts/password_change/', [name='password_change'],
    # path('accounts/password_change/done/', [name='password_change_done'],
    # path('accounts/password_reset/', [name='password_reset'],
    # path('accounts/password_reset/done/', [name='password_reset_done'],
    # path('accounts/reset/<uidb64>/<token>/', [name='password_reset_confirm'],
    # path('accounts/reset/done/', [name='password_reset_complete'],
]
