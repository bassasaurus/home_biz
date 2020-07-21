from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from transactions.models import Transactions, Accounts, BusinessGroups, Categories
from django.db.models import Sum


@receiver(post_save, sender=Transactions)
def update_accounts(sender, instance, dispatch_uid='update_accounts', **kwargs):

    account = Accounts.objects.get(pk=instance.accounts.pk)

    account_total = Transactions.objects.filter(accounts=instance.accounts.pk).aggregate(Sum('amount'))

    account.balance = account_total.get('amount__sum')
    account.save()



@receiver(post_save, sender=Transactions)
def update_business_groups(sender, instance, dispatch_uid='update_business_groups', **kwargs):

    business = BusinessGroups.objects.get(pk=instance.business_groups.pk)

    business_total = Transactions.objects.filter(business_groups=instance.business_groups.pk).aggregate(Sum('amount'))

    business.balance = business_total.get('amount__sum')
    business.save()


@receiver(post_save, sender=Transactions)
def update_categories(sender, instance, dispatch_uid='update_categories', **kwargs):

    category = Categories.objects.get(pk=instance.categories.pk)

    category_total = Transactions.objects.filter(categories=instance.categories.pk).aggregate(Sum('amount'))

    category.balance = category_total.get('amount__sum')
    category.save()
