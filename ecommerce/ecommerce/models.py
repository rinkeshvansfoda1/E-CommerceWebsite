from django.db import models

class Product(models.Model):
    Product_Name=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='photo')
    Description=models.TextField()
    Price=models.IntegerField()
    Offer=models.BooleanField(default=False)
    

class Product_laptop(models.Model):
    Product_Name=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='photo')
    Description=models.TextField()
    Price=models.IntegerField()
    Offer=models.BooleanField(default=False)

class Product_washing_machine(models.Model):
    Product_Name=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='photo')
    Description=models.TextField()
    Price=models.IntegerField()
    Offer=models.BooleanField(default=False)


class Product_phone(models.Model):
    Product_Name=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='photo')
    Description=models.TextField()
    Price=models.IntegerField()
    Offer=models.BooleanField(default=False)

class Product_smarttv(models.Model):
    Product_Name=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='photo')
    Description=models.TextField()
    Price=models.IntegerField()
    Offer=models.BooleanField(default=False)

class Product_jeans(models.Model):
    Product_Name=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='photo')
    Description=models.TextField()
    Price=models.IntegerField()
    Offer=models.BooleanField(default=False)

# class Category(models.Model):
#     name = models.CheckConstraint(max_lenght=200)