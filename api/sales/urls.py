from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DailySalesViewSets

router = DefaultRouter()
router.register(r'sales', DailySalesViewSets, basename='user')
urlpatterns = router.urls