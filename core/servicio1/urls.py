from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MiModeloViewSet

router = DefaultRouter()
router.register(r'mimodelo', MiModeloViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mimodelo/', MiModeloViewSet.as_view({'get': 'list'})),

]
