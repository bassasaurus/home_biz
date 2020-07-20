from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions.models import Transactions, Accounts, BusinessGroups


@receiver(post_save, sender=Transactions)
def update_accounts(sender, instance, dispatch_uid='update_accounts', **kwargs):

    account = Accounts.objects.get(pk=instance.accounts.pk)

    if instance.type == 'Debit':
        updated_balance = instance.accounts.balance - instance.amount
        account.balance = updated_balance
        account.save()


    if instance.type == 'Credit':
        updated_balance = account.balance + instance.amount
        account.balance = updated_balance
        account.save()

@receiver(post_save, sender=Transactions)
def update_business_groups(sender, instance, dispatch_uid='update_business_groups', **kwargs):

    business = BusinessGroups.objects.get(pk=instance.business_groups.pk)

    if instance.type == 'Debit':
        updated_balance = instance.businesss.balance - instance.amount
        business.balance = updated_balance
        business.save()


    if instance.type == 'Credit':
        updated_balance = business.balance + instance.amount
        business.balance = updated_balance
        business.save()
