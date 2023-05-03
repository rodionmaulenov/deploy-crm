from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save

from customers.models import Customer


def create_customer(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(user=instance, name=instance.username)
        print('Create Customer')


post_save.connect(create_customer, sender=User)

# def update_customer(sender, instance, created, **kwargs):
#     if created == False:
#         instance.customer.save()
#         print('Update Customer')
