# Create your views here.
from rest_framework import viewsets, mixins

from .models import Blog, CategoryBlog
from .serializers import BlogSerializer, CategorySerializer


class BlogViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Blog.objects.all().order_by('-date_created')
    serializer_class = BlogSerializer
    permission_classes = ()


class CategoryViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = CategoryBlog.objects.all().order_by('-date_created')
    serializer_class = CategorySerializer
    permission_classes = ()
