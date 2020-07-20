from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions.models import Transactions, Accounts, Categories, BusinessGroups


@receiver(post_save, sender=Transactions)
def update_accounts(sender, instance, dispatch_uid='update_accounts', **kwargs):


    print("Request finished!")
