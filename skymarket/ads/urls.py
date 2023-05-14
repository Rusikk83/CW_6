from django.urls import include, path

# TODO настройка роутов для модели

from rest_framework import routers

from ads.views import AdViewSet

router_ad = routers.SimpleRouter()
router_ad.register('ad', AdViewSet)

