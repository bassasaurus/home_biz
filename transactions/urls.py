from django.urls import path
from transactions.views import (
    TransactionsListView, TransactionsCreateView, TransactionsDeleteView, TransactionsDetailView, TransactionsUpdateView,
    BusinessGroupsListView, BusinessGroupsCreateView, BusinessGroupsDeleteView, BusinessGroupsDetailView, BusinessGroupsUpdateView,
    AccountsListView, AccountsCreateView, AccountsUpdateView, AccountsDetailView, AccountsDeleteView,
    CategoriesListView, CategoriesCreateView, CategoriesUpdateView, CategoriesDetailView, CategoriesDeleteView,
    AccountsAutocomplete, CategoriesAutocomplete, BusinessGroupsAutocomplete)
from transactions.models import Accounts

urlpatterns = [

    path('accounts_autocomplete/', AccountsAutocomplete.as_view(create_field='name'), name='accounts_autocomplete'),
    path('categories_autocomplete/', CategoriesAutocomplete.as_view(create_field='name'), name='categories_autocomplete'),
    path('business_groups_autocomplete/', BusinessGroupsAutocomplete.as_view(create_field='name'), name='business_groups_autocomplete'),

    path('transactions/list/', TransactionsListView.as_view(), name='transactions_list'),
    path('transactions/create/', TransactionsCreateView.as_view(), name='transactions_create'),
    path('tranactions/detail/<pk>', TransactionsDetailView.as_view(), name='transactions_detail'),
    path('transactions/update/<pk>', TransactionsUpdateView.as_view(), name='transactions_update'),
    path('tranactions/delete/<pk>', TransactionsDeleteView.as_view(), name='transactions_delete'),

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

    path('categories/list/', CategoriesListView.as_view(), name='categories_list'),
    path('categories/create/', CategoriesCreateView.as_view(), name='categories_create'),
    path('categories/detail/<pk>', CategoriesDetailView.as_view(), name='categories_detail'),
    path('categories/update/<pk>', CategoriesUpdateView.as_view(), name='categories_update'),
    path('categories/delete/<pk>', CategoriesDeleteView.as_view(), name='categories_delete'),
]
