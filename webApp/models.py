from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#How much that i spent money today and for what? 
class out_comes(models.Model):

    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User ,on_delete=models.CASCADE)


#How much that i get money today and how I reach it ? 
class in_comes(models.Model):
    text=models.CharField( max_length=250)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
