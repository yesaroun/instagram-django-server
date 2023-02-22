from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import UserSerializer


class FeedSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Feed
        fields = "__all__"  # Model의 전체 field 가져옴
        # depth = 1  # 더 낮은 단계 객체까지 가져옴
        # depth로 받아오는 방식은 포린키로 받아오는 모든 user 객체 정보를 가져오기에
        # 위에 user = UserSerializer()를 받아와서 그것만 가져온다.
