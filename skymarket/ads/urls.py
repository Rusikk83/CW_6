from django.urls import include, path

# TODO настройка роутов для модели

from rest_framework import routers

from ads.views import AdViewSet, CommentViewSet, AdMeViewSet

router_ad = routers.SimpleRouter()
router_ad.register('', AdViewSet)

router_comment = routers.SimpleRouter()
router_comment.register('comments', CommentViewSet)

router_ads_me = routers.SimpleRouter()
router_ads_me.register('', AdMeViewSet)
