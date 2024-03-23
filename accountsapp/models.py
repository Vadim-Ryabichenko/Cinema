from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    wallet = models.DecimalField(decimal_places=2, max_digits=10, default=10000)
    amount_spent = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    photo = models.ImageField(upload_to='profile_photos', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} like a {self.username}'


