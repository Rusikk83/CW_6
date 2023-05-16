from datetime import datetime

from rest_framework import serializers

from ads.models import Ad
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


class AdCreateSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='email', queryset=User.objects.all(), required=False)


    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = request.user
        validated_data['created_at'] = str(datetime.now())
        return super().create(validated_data)

    class Meta:
        fields = '__all__'
        model = Ad
