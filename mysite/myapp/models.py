from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=200)
    price=models.IntegerField()
    rent=models.IntegerField()
    tax=models.IntegerField()
    Emi=models.IntegerField()
    exp=models.IntegerField()
    net_exp=models.IntegerField(default=0)
    net_income=models.IntegerField(default=0)



# Create your models here.
