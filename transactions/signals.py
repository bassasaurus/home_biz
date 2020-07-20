from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions.models import Transactions, Accounts


@receiver(post_save, sender=Transactions)
def update_accounts(sender, instance, dispatch_uid='update_accounts', **kwargs):

    account = Accounts.objects.get(pk=instance.accounts.pk)

    if instance.type == 'Debit':
        updated_balance = instance.accounts.balance - instance.amount
        account.balance = updated_balance
        account.save()
        print(account.name, account.balance)

    if instance.type == 'Credit':
        updated_balance = account.balance + instance.amount
        account.balance = updated_balance
        account.save()
        print(account.name, account.balance)
