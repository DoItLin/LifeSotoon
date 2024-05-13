from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Token for athuriseing 
class Token(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    token=models.CharField(max_length=128)
    def __str__(self):
        return "The {}'s token is: {}".format(self.user,self.token)

#How much that i spent money today and for what? 
class out_comes(models.Model):

    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    def __str__(self):
        return "در روز{}. مبلغ {} خرج کردی".format(self.date ,self.amount)
  
#How much that i get money today and how I reach it ? 
class in_comes(models.Model):
    text=models.CharField( max_length=250)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    def __str__(self):
        return "در روز{}. مبلغ {} بدست آوردی.".format(self.date ,self.amount)
 
