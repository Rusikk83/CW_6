from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

#from users.models import User





User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        #fields = "__all__"
        exclude = ['last_login', 'role']

# class UserSerializer(BaseUserRegistrationSerializer):
#     class Meta:
#         model = User
#         #fields = "__all__"
#         exclude = ['last_login', 'role']



class CurrentUserSerializer(serializers.ModelSerializer):
    pass
