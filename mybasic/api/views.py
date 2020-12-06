from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Blog 
from .serializers import BlogSerializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def Bloglist(request):
    if request.method == 'GET':
        blogs=Blog.objects.all()
        serializer = BlogSerializers(blogs,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data =JSONParser().parse(request)
        serializer =BlogSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)

        return JsonResponse(serializer.errors,status=400)



@csrf_exempt
def Blog_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogSerializers(blog)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlogSerializers(blog, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        blog.delete()
        return HttpResponse(status=204)