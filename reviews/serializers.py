from rest_framework.serializers import ModelSerializer

from users.serializers import UserSerializer
from .models import Review


class ReviewSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = "__all__"
