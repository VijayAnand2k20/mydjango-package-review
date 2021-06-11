from django.contrib.auth import get_user_model
from django.db import models
from allauth.account.signals import user_logged_in

User = get_user_model()

def user_logged_in_reciever(request, user, **kwargs):
    print(request)
    print(user)


user_logged_in.connect(user_logged_in_reciever, sender=User)