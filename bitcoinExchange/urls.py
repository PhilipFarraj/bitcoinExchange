from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from bitcoinExchange import views

router = routers.DefaultRouter()
router.register(r'api/v1/quotes', views.ExchangeRateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
