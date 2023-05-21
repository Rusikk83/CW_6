from rest_framework import pagination, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, AdCreateSerializer, CommentSerializer

from ads.permissions import IsAuthor, IsAdmin


class AdPagination(pagination.PageNumberPagination):
    PAGE_SIZE = 8


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.order_by('created_at')
    default_serializer_class = AdSerializer
    # permission_classes = [AllowAny]
    pagination_class = AdPagination

    default_permission = [AllowAny]
    #
    permissions = {
        "create": [IsAuthenticated],
        "update": [IsAuthenticated, IsAuthor | IsAdmin],
        "partial_update": [IsAuthenticated, IsAuthor | IsAdmin],
        "destroy": [IsAuthenticated, IsAuthor | IsAdmin],
        "retrieve": [IsAuthenticated, IsAuthor | IsAdmin],
    }
    #
    serializers = {
        "list": AdSerializer,
        "create": AdCreateSerializer,
        "retrieve": AdDetailSerializer,
     }
    #
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)
    #
    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]


class AdMeViewSet(viewsets.ModelViewSet):

    http_method_names = ['get']
    queryset = Ad.objects.order_by('created_at')
    default_serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = AdPagination


    def list(self, request, *args, **kwargs):

        self.queryset = self.queryset.filter(author=request.user)
        return super().list(request, *args, **kwargs)


    serializers = {
        "list": AdSerializer,
        "retrieve": AdDetailSerializer,
     }
    #
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)
    #
    # def get_permissions(self):
    #     return [permission() for permission in self.permissions.get(self.action, self.default_permission)]






class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.order_by('created_at')
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    pagination_class = AdPagination


    def list(self, request, *args, **kwargs):
        ad_pk = request.parser_context['kwargs']['ad_pk']
        self.queryset = self.queryset.filter(ad_id=ad_pk)
        return super().list(request, *args, **kwargs)


    default_permission = [IsAuthenticated]

    permissions = {

        "update": [IsAuthenticated, IsAuthor | IsAdmin],
        "partial_update": [IsAuthenticated, IsAuthor | IsAdmin],
        "destroy": [IsAuthenticated, IsAuthor | IsAdmin],
        "retrieve": [IsAuthenticated, IsAuthor | IsAdmin],
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]
