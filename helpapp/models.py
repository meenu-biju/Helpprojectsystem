from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    phone = models.IntegerField()
    city = models.CharField(max_length=250)
    message = models.CharField(max_length=250)


class Predonation(models.Model):
    Pre_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    city = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    bank = models.CharField(max_length=250)
    accno = models.IntegerField()
    amount = models.IntegerField()
    check = models.CharField(max_length=250)


