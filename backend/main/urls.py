from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'deadline',DeadlineView)

urlpatterns = router.urls