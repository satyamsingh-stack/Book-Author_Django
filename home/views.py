from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.views import APIView

# Create your views here.
class Operation1(APIView):
    def post(self,request):
        serializer=AuthorSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        item=Author.objects.all()
        serializer=AuthorSerializer(item,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Operation2(APIView):
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        temp_id=request.data.get('author_id')
        if(serializer.is_valid() and Author.objects.filter(id=temp_id).exists()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response("objects does not exists",status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,id):
        try:
            item=Book.objects.get(id=id)
            serializer=BookSerializer(item)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response("Not Found",status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        try:
            item=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response("Not Found",status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response("deleted",status=status.HTTP_204_NO_CONTENT)
    
    def patch(self,request,id):
        try:
            item=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response("not found",status=status.HTTP_404_NOT_FOUND)
        serializer=BookSerializer(item,data=request.data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response("Updated Partially",status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

        
