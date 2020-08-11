from django import forms
from transactions.models import Transactions
from dal import autocomplete


class DateInput(forms.DateInput):
    input_type = 'date'


class TransactionsForm(forms.ModelForm):

    class Meta:
        model = Transactions
        fields = ['name', 'date', 'amount', 'type', 'accounts', 'categories', 'business_groups', 'comments']
        widgets = {
            'date': DateInput(),
            'accounts': autocomplete.ModelSelect2(url='accounts_autocomplete'),
            'categories': autocomplete.ModelSelect2(url='categories_autocomplete'),
            'business_groups': autocomplete.ModelSelect2(url='business_groups_autocomplete')
        }
