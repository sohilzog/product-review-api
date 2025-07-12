# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pro_app.views import ProductViewSet, ReviewViewSet
from django.contrib import admin


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
