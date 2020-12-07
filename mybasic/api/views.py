from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Blog 
from .serializers import BlogSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET', 'POST'])
def Bloglist(request):
    if request.method == 'GET':
        blogs=Blog.objects.all()
        serializer = BlogSerializers(blogs,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        
        serializer =BlogSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def Blog_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializers(blog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        serializer = BlogSerializers(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blog.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)