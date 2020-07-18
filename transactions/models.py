from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


# https://github.com/django-money/django-money

class Accounts(models.Model):

    class Meta:
        verbose_name_plural = "Accounts"

    created_by = models.ForeignKey(
        User, models.SET_NULL, editable=False, blank=True, null=True, related_name="account_created_by")
    updated_by = models.ForeignKey(
        User, models.SET_NULL, editable=False, blank=True, null=True, related_name="account_updated_by")
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200)
    balance = MoneyField(max_digits=14, decimal_places=2,
                        default_currency='USD', default=0.00)

    def __str__(self):
        created_by = str(self.created_by)
        updated_by = str(self.updated_by)
        created_timestamp = str(self.created_timestamp.strftime('%D%M %H:%M'))
        updated_timestamp = str(self.updated_timestamp.strftime('%D%M %H:%M'))
        return str(self.name + ' | ' + 'created by: ' + created_by + ' at: ' + created_timestamp + ' | ' + 'updated_by: ' + updated_by + ' at: ' + updated_timestamp)


class BusinessGroups(models.Model):

    class Meta:
        verbose_name_plural = "Business Groups"

    created_by = models.ForeignKey(User, models.SET_NULL, editable=False,
                                   blank=True, null=True, related_name="business_created_by")
    updated_by = models.ForeignKey(User, models.SET_NULL, editable=False,
                                   blank=True, null=True, related_name="business_updated_by")
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200)
    balance = MoneyField(max_digits=14, decimal_places=2,
                        default_currency='USD', default=0.00)

    def __str__(self):
        created_by = str(self.created_by)
        updated_by = str(self.updated_by)
        created_timestamp = str(self.created_timestamp.strftime('%D%M %H:%M'))
        updated_timestamp = str(self.updated_timestamp.strftime('%D%M %H:%M'))
        return str(self.name + ' | ' + 'created by: ' + created_by + ' at: ' + created_timestamp + ' | ' + 'updated_by: ' + updated_by + ' at: ' + updated_timestamp)


class Categories(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    created_by = models.ForeignKey(User, models.SET_NULL, editable=False,
                                   blank=True, null=True, related_name="category_created_by")
    updated_by = models.ForeignKey(User, models.SET_NULL, editable=False,
                                   blank=True, null=True, related_name="category_updated_by")
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200)

    def __str__(self):
        created_by = str(self.created_by)
        updated_by = str(self.updated_by)
        created_timestamp = str(self.created_timestamp.strftime('%D%M %H:%M'))
        updated_timestamp = str(self.updated_timestamp.strftime('%D%M %H:%M'))
        return str(self.name + ' | ' + 'created by: ' + created_by + ' at: ' + created_timestamp + ' | ' + 'updated_by: ' + updated_by + ' at: ' + updated_timestamp)


class Transactions(models.Model):

    TRANSACTION_CHOICES = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit')
    ]

    class Meta:
        verbose_name_plural = "Transactions"

    created_by = models.ForeignKey(
        User, models.SET_NULL, editable=False, blank=True, null=True, related_name="payee_created_by")
    updated_by = models.ForeignKey(
        User, models.SET_NULL, editable=False, blank=True, null=True, related_name="payee_updated_by")
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200)
    date = models.DateField()
    amount = MoneyField(max_digits=14, decimal_places=2,
                        default_currency='USD', default=0.00)
    type = models.CharField(max_length=6, choices=TRANSACTION_CHOICES)
    accounts = models.ForeignKey(Accounts, models.SET_NULL, null=True)
    categories = models.ForeignKey(Categories, models.SET_NULL, null=True)
    business_groups = models.ForeignKey(
        BusinessGroups, models.SET_NULL, null=True)
    comments = models.CharField(max_length=500, default='', blank=True)

    def __str__(self):
        created_by = str(self.created_by)
        updated_by = str(self.updated_by)
        amount = str(self.amount)
        created_timestamp = str(self.created_timestamp.strftime('%D%M %H:%M'))
        updated_timestamp = str(self.updated_timestamp.strftime('%D%M %H:%M'))
        return str(self.name + ' - ' + amount + ' | ' + 'created by: ' + created_by)
