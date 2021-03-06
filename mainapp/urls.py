from django.urls import path, include
from rest_framework import routers

from mainapp.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
