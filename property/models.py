from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User,auth

class Property(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=25,default="Cottage villa")
    city=models.CharField(max_length=25)
    society=models.CharField(max_length=25)
    locality=models.CharField(max_length=25)
    house_no=models.CharField(max_length=10)
    bedrooms=models.IntegerField()
    bathrooms=models.IntegerField()
    area=models.IntegerField()
    age=models.CharField(max_length=10)
    price=models.CharField(max_length=15)
    desc=models.TextField()
    img=models.ImageField(upload_to ='uploads/')
    contactno=models.BigIntegerField(default=9995556457)
    def _str_(self):
        return self.seller


class Land(models.Model):
    landseller=models.ForeignKey(User,on_delete=models.CASCADE)
    type=models.CharField(max_length=25)
    city=models.CharField(max_length=25)
    area=models.IntegerField()
    locality=models.CharField(max_length=25)
    price=models.CharField(max_length=15)
    contactno=models.BigIntegerField(default=9995556457)
    img=models.ImageField(upload_to ='uploads/',default='real-estate-ga1b304591_640.jpg')
    def _str_(self):
        return self.landseller

class Buyer(models.Model):
    buyer=models.ForeignKey(User,on_delete=models.CASCADE)
    incomecertificate=models.ImageField(upload_to ='uploads/')
    phoneno=models.BigIntegerField()
    email=models.EmailField()
    photo=models.ImageField(upload_to ='uploads/')
    card=models.ImageField(upload_to ='uploads/')
    def _str_(self):
        return self.buyer