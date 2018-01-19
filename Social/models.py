from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    likes_cheese = models.BooleanField(default=False)
    favorite_ham_name = models.CharField(max_length=250)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])