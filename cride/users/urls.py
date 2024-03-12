"""Users URLs"""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import users as user_views

router = DefaultRouter()# This is the router that is going to be used
router.register(r'users', user_views.UserViewSet, basename='users')# This is the view that is going to be registered in the router

urlpatterns = [
    path('', include(router.urls))
]
