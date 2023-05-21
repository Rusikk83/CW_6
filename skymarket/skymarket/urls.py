from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.urls import users_router

from ads.urls import router_ad, router_comment

# TODO здесь необходимо подклюючит нужные нам urls к проекту

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("api/", include(users_router.urls)),
    path("api/", include(router_ad.urls)),
    path("api/ads/<int:ad_pk>/", include(router_comment.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    #path("users/", include('users.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
