from datetime import datetime

from rest_framework import serializers

from ads.models import Ad, Comment


from users.models import User


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою


class CommentSerializer(serializers.ModelSerializer):

    """
    Почему то не получилось получить правильное значение для картинки пользователя (ссылки).
    Поэтому лого в комментариях не отображаются.
    Поле author_image через @property в модели перредает только локальную ссылку, тоже не работает
    """

    #author_image = serializers.SlugRelatedField(slug_field='image', queryset=User.objects.all(), required=False)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = request.user
        validated_data['created_at'] = str(datetime.now())
        validated_data['ad_id'] = request.parser_context['kwargs']['ad_pk']
        return super().create(validated_data)


    class Meta:
        fields = [
            "pk",
            "text",
            "author_id",
            "created_at",
            "author_first_name",
            "author_last_name",
            "ad_id",
            "author_image",
        ]
        model = Comment

class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad

        fields = ['pk', "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели


    class Meta:
        fields = [
            'pk',
            'image',
            'title',
            'price',
            'phone',
            'description',
            'author_first_name',
            'author_last_name',
            'author_id',
        ]

        model = Ad


class AdCreateSerializer(serializers.ModelSerializer):



    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = request.user
        validated_data['created_at'] = str(datetime.now())
        return super().create(validated_data)

    class Meta:
        fields = [
            'pk',
            'image',
            'title',
            'price',
            'phone',
            'description',
            'author_first_name',
            'author_last_name',
            'author_id',
        ]
        model = Ad
