# TODO Part 1: Import UserCreateSerializer and UserSerializer from djoser.serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import User
# TODO Part 1: Create a CustomUserCreateSerializer extending djoser's UserCreateSerializer
#              with fields: id, username, password, email, role, full_name, bio, status
class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "username", "password", "email", "role", "full_name", "bio", "status")
# TODO Part 1: Create a CustomUserSerializer extending djoser's UserSerializer
#              with fields: id, username, email, role, full_name, bio, status
class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        field = ("id", "username", "email", "role", "full_name", "bio", "status")
