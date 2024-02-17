from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=70, primary_key=True)
    password = models.CharField(max_length=70)

class Purchases(models.Model):
    purchase = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()