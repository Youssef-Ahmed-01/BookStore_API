from django.contrib import admin
from .models import Book, Author, Order, User
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(User)
admin.site.register(Order)
