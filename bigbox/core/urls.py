""" core URLs """

# Django
from django.urls import path, re_path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import CategoryViewSet as category_views
from .views import BoxViewSet as box_views
from .views import ActivityViewSet as activity_views


router = DefaultRouter()
router.register(r'category', category_views, basename='category')
router.register(r'boxes', box_views, basename='boxes')
router.register(r'activities', activity_views, basename='activities')


urlpatterns = [
] + router.urls
