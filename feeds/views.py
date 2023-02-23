from django.shortcuts import render
from rest_framework.exceptions import NotFound

from .models import Feed
from users.models import User
from rest_framework.views import APIView
from .serializers import FeedSerializer, FeedDetailSerializer, UserFeedsSerializer
from rest_framework.response import Response


# 내가 짠 코드
# class Feeds(APIView):
#     def get(self, request):
#         feeds = Feed.objects.all()
#         serializer = FeedSerializer(feeds, many=True)
#         return Response(serializer.data)


class AllFeeds(APIView):
    """전체 게시글을 불러오는 api"""

    def get(self, request):
        all_feeds = Feed.objects.all()
        serializer = FeedSerializer(all_feeds, many=True)
        return Response(serializer.data)


class FeedDetail(APIView):
    """특정 feed의 상세 내용을 불러오는 api"""

    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound

    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        serializer = FeedDetailSerializer(feed)
        return Response(serializer.data)


class UserFeeds(APIView):
    """username을 받아서 user의 게시글을 불러오는 api"""

    def get_objects(self, username):
        try:
            user_id = User.objects.get(username=username).id
            print("user_id", user_id)
            return Feed.objects.filter(user=user_id)
        except Feed.DoesNotExist:
            raise NotFound

    def get(self, request, username):
        feeds = self.get_objects(username)
        print("user_feeds", username)
        serializer = UserFeedsSerializer(feeds, many=True)
        return Response(serializer.data)
