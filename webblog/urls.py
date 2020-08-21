from django.urls import path

from rest_framework import routers
from .views import CategoryViewSet, BlogViewSet

router = routers.SimpleRouter()
router.register('blog', BlogViewSet)
router.register('category', CategoryViewSet)

urlpatterns = []

urlpatterns += router.urls
