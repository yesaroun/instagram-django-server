from rest_framework.serializers import ModelSerializer
from .models import Feed


class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"  # Model의 전체 field 가져옴
        depth = 1
