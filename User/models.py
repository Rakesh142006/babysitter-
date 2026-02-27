from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.email

class Sitters_category(models.Model):
    type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='sitter_cat')