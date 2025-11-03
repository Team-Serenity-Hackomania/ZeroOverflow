from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DustBinViewSet

router = DefaultRouter()
router.register(r'dustbin', DustBinViewSet, basename='dustbin')

urlpatterns = [
    path('', include(router.urls)),
]