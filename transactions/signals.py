from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from transactions.models import Transactions, Accounts, BusinessGroups, Categories
from django.db.models import Sum


@receiver(post_save, sender=Transactions)
def update_accounts(sender, instance, dispatch_uid='update_accounts', **kwargs):

    account = Accounts.objects.get(pk=instance.accounts.pk)

    transaction = Transactions.objects.get(pk=instance.pk)

    account_total = Transactions.objects.filter(accounts=instance.accounts.pk).aggregate(Sum('amount'))


    account.balance = account_total.get('amount__sum')
    account.save()



# @receiver(post_save, sender=Transactions)
# def update_business_groups(sender, instance, dispatch_uid='update_business_groups', **kwargs):
#
#     business = BusinessGroups.objects.get(pk=instance.business_groups.pk)
#
#     business_queryset = Transactions.objects.filter(business_groups=instance.business_groups).aggregate(Sum('amount'))
#
#     if instance.type == 'Debit':
#         updated_balance = business.balance - instance.amount
#         business.balance = updated_balance
#         business.save()
#
#
#     if instance.type == 'Credit':
#         updated_balance = business.balance + instance.amount
#         business.balance = updated_balance
#         business.save()


# @receiver(post_save, sender=Transactions)
# def update_categories(sender, instance, dispatch_uid='update_categories', **kwargs):
#
#     category = Categories.objects.get(pk=instance.categories.pk)
#
#     category_queryset = Transactions.objects.filter(categories=instance.categories).aggregate(Sum('amount'))
#
#
#     if instance.type == 'Debit':
#         updated_balance = category.balance - instance.amount
#         category.balance = updated_balance
#         category.save()
#
#
#     if instance.type == 'Credit':
#         updated_balance = category.balance + instance.amount
#         category.balance = updated_balance
#         category.save()
