from rest_framework import  serializers
from .models import Book, Author, Order, User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'author_n']
        depth = 1 
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'order', 'name', 'phone']

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  
    book = BookSerializer(read_only=True) 
    total_price = serializers.SerializerMethodField( method_name='get_total_price' )
    
    class Meta:
        model = Order
        fields = '__all__'
    
    def get_total_price(self, obj):
        book_price = obj.book.price 
        return float(book_price) + float(book_price) * 0.15
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

