import os

from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404

from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Book, Author, Order, User
from .serializers import UserSerializer, BookSerializer, OrderSerializer, AuthorSerializer

# Create your views here.
def no_rest_no_model(request):
    users = [
        {
            'id' : 1,
            'name' : 'omar',
            'phone' : 1234567
        },
        {
            'id' : 2,
            'name' : 'youou',
            'phone' : 7654321
        },
    ]
    return JsonResponse(users, safe=False)
 
    

def no_rest_with_model(request):
    usersd = User.objects.all()
    booksd = Book.objects.all()
    
    response = {
        'users' : list(usersd.values('name', 'phone', 'address', 'email')),
        'books' : list(booksd.values('title'))
    }
    return JsonResponse(response, safe=False)

 
#get post
@api_view(['GET', 'POST'])
def FBV_List(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)
    elif request.method  == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def FBV_PK(request, pk):
    try:
        user = User.objects.get(pk = pk)
    except user.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method  == 'PUT':
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_301_MOVED_PERMANENTLY)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method  == 'DELETE':
        user.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
class CBV_List(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )


#4.2 GET PUT DELETE class based views -- pk 
class  CBV_pk(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExists:
            raise Http404
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class viewsets_user(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class viewsets_book(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backend = [filters.SearchFilter]
    search_fields = ['title']

class viewsets_order(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class viewsets_author(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer