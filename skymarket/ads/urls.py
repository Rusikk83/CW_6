from django.urls import include, path

# TODO настройка роутов для модели

from rest_framework import routers

from ads.views import AdViewSet, CommentViewSet

router_ad = routers.SimpleRouter()
router_ad.register('ad', AdViewSet)

router_comment = routers.SimpleRouter()
router_comment.register('comment', CommentViewSet)

