
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import StandardUser

def standard_user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='student')
        instance.groups.add(group)
        StandardUser.objects.create(user=instance, name=instance.username)
    print('Profile created!')

post_save.connect(standard_user_profile, sender=User)