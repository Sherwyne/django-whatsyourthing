from django.db import models

# Create your models here.
class Registrant(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    date_registered = models.DateField(null=True, auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name