from django.urls import path
from transactions.views import (
            IndexView, HomeView, TransactionsListView, TransactionsCreateView,
            TransactionsDeleteView, TransactionsDetailView, TransactionsUpdateView,
            BusinessGroupsListView, BusinessGroupsCreateView, BusinessGroupsDeleteView,
            BusinessGroupsDetailView, BusinessGroupsUpdateView, AccountsListView, AccountsCreateView,
            AccountsUpdateView, AccountsDetailView, AccountsDeleteView
            )

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),

    path('transactions/list/', TransactionsListView.as_view(), name='transactions_list'),
    path('transactions/create/', TransactionsCreateView.as_view(), name='transactions_create'),
    path('tranactions/detail/<pk>', TransactionsDetailView.as_view(), name='transactions_detail'),
    path('transactions/update/<pk>', TransactionsUpdateView.as_view(), name='transactions_update'),
    path('trandactions/delete/<pk>', TransactionsDeleteView.as_view(), name='transactions_delete'),

    path('business/list/', BusinessGroupsListView.as_view(), name='business_list'),
    path('business/create/', BusinessGroupsCreateView.as_view(), name='business_create'),
    path('business/detail/<pk>', BusinessGroupsDetailView.as_view(), name='business_detail'),
    path('business/update/<pk>', BusinessGroupsUpdateView.as_view(), name='business_update'),
    path('business/delete/<pk>', BusinessGroupsDeleteView.as_view(), name='business_delete'),

    path('accounts/list/', AccountsListView.as_view(), name='accounts_list'),
    path('accounts/create/', AccountsCreateView.as_view(), name='accounts_create'),
    path('accounts/detail/<pk>', AccountsDetailView.as_view(), name='accounts_detail'),
    path('accounts/update/<pk>', AccountsUpdateView.as_view(), name='accounts_update'),
    path('accounts/delete/<pk>', AccountsDeleteView.as_view(), name='accounts_delete'),

]
