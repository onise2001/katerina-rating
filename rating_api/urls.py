from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RatingViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'rating',RatingViewSet)


urlpatterns = [
    path('', include(router.urls))
]
