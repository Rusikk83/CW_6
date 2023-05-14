from rest_framework import serializers

from  ads.models import Ad
from rest_framework.relations import SlugRelatedField

from users.models import User


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad

        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        author_first_name = SlugRelatedField(slug_field='first_name', queryset=User.objects.all())
        author_last_name = SlugRelatedField(slug_field='last_name', queryset=User.objects.all())
        author_id = SlugRelatedField(slug_field='user_id', queryset=User.objects.all())

        fields = '__all__'