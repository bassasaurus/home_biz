from django import forms
from transactions.models import Transactions


class DateInput(forms.DateInput):
    input_type = 'date'


class TransactionsForm(forms.ModelForm):


    class Meta:
        model = Transactions
        fields = ['name', 'date', 'amount', 'type', 'accounts', 'categories', 'business_groups', 'comments']
        widgets = {
            'date': DateInput()
        }
