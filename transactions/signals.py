from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions.models import Transactions, Accounts, BusinessGroups, Categories
from django.db.models import Sum


@receiver(post_save, sender=Transactions)
def update_accounts(sender, instance, dispatch_uid='update_accounts', **kwargs):

    account = Accounts.objects.get(pk=instance.accounts.pk)

    tranactions_queryset = Transactions.objects.filter(accounts=instance.accounts).aggregate(Sum('amount'))

    account_total = tranactions_queryset.get('amount__sum')

    if instance.type == 'Debit':
        updated_balance = account_total - instance.amount
        account.balance = updated_balance
        account.save()

    if instance.type == 'Credit':
        updated_balance = account_total + instance.amount
        account.balance = updated_balance
        account.save()

@receiver(post_save, sender=Transactions)
def update_business_groups(sender, instance, dispatch_uid='update_business_groups', **kwargs):

    business = BusinessGroups.objects.get(pk=instance.business_groups.pk)

    business_queryset = Transactions.objects.filter(accounts=instance.accounts).aggregate(Sum('amount'))

    business_total = business_queryset.get('amount__sum')

    if instance.type == 'Debit':
        updated_balance = business_total - instance.amount
        business.balance = updated_balance
        business.save()


    if instance.type == 'Credit':
        updated_balance = business_total + instance.amount
        business.balance = updated_balance
        business.save()


@receiver(post_save, sender=Transactions)
def update_categories(sender, instance, dispatch_uid='update_categories', **kwargs):

    category = Categories.objects.get(pk=instance.categories.pk)

    category_queryset = Transactions.objects.filter(accounts=instance.accounts).aggregate(Sum('amount'))

    category_total = category_queryset.get('amount__sum')

    if instance.type == 'Debit':
        updated_balance = category_total - instance.amount
        category.balance = updated_balance
        category.save()


    if instance.type == 'Credit':
        updated_balance = category_total + instance.amount
        category.balance = updated_balance
        category.save()
