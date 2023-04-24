from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'User', UserViewSet)
router.register(r'Mattress', MattressViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', CustomObtainAuthToken.as_view()),
]