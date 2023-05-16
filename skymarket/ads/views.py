from rest_framework import pagination, viewsets
from rest_framework.permissions import AllowAny

from ads.models import Ad
from ads.serializers import AdSerializer, AdDetailSerializer, AdCreateSerializer




class AdPagination(pagination.PageNumberPagination):
    PAGE_SIZE = 8


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.order_by('created_at')
    default_serializer_class = AdSerializer
    permission_classes = [AllowAny]
    pagination_class = AdPagination

    # default_permission = [AllowAny] # требуется расширить
    #
    # permissions = {
    #     "create": [IsAuthenticated],
    #     "update": [IsAuthenticated, IsOwner | IsModerator],
    #     "partial_update": [IsAuthenticated, IsOwner | IsModerator],
    #     "destroy": [IsAuthenticated, IsOwner | IsModerator]
    # }
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
    # def get_permissions(self):
    #     return [permission() for permission in self.permissions.get(self.action, self.default_permission)]





class CommentViewSet(viewsets.ModelViewSet):
    pass

