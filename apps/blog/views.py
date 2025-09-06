# blog/views.py
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by("-date")
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "slug"
