from django.db import models
from django.contrib.auth import models as mod
# Create your models here.


class User(mod.User, mod.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
