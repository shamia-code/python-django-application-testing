from django.db import models


from django.contrib.auth.models import AbstractUser 

class MyUser(AbstractUser):
    def deactivate(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()
    
    @property
    def active(self):
        return self.is_active
    