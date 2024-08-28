from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import PostApi


router = DefaultRouter()
router.register(r'posts', PostApi, basename='posts')


urlpatterns = router.urls