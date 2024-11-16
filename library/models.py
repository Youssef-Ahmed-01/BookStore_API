from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Author(models.Model):
    author_n = models.CharField(max_length=50)
    
    def __str__(self):
        return self.author_n
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author_n = models.ForeignKey(Author, related_name='book', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='order', on_delete=models.CASCADE)
    total_price = models.FloatField()
    s_time = models.TimeField("date published")
    
    def __str__(self):
        return f'{self.user} +   {self.book}'

    
    
    
