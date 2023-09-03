from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FileViewSet

router = DefaultRouter()
router.register(r'majoo', FileViewSet, basename='user')
urlpatterns = router.urls