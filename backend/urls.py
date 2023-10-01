from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoView


router = DefaultRouter()
router.register(r'vidoes', VideoView)

urlpatterns = [
    path('', include(router.urls)),
]