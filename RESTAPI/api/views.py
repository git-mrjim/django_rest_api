from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    lookup_field = "pk"

class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get('title', '')

        if title:
            blog_posts = BlogPost.objects.filter(title_icontains=title)
        else:
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializers(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BlogPostListOne(APIView):
    def get(self, request, pk, format=None):
        blog_post = get_object_or_404(BlogPost, pk=pk) 

        serializer = BlogPostSerializers(blog_post)
        return Response(serializer.data, status=status.HTTP_200_OK)