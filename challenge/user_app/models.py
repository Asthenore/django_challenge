from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass

    def inverted_name(self):
        return f"{self.last_name}, {self.first_name}"
    
