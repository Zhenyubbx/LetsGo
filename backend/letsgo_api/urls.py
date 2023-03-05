from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import EventViewSet, OutingViewSet, UserViewSet, AttractionViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('events', EventViewSet)
router.register('outings', OutingViewSet)
router.register('attractions', AttractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
