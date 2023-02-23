from django.shortcuts import render
from rest_framework.exceptions import NotFound

from .models import Feed
from rest_framework.views import APIView
from .serializers import FeedSerializer, FeedDetailSerializer
from rest_framework.response import Response


# 내가 짠 코드
# class Feeds(APIView):
#     def get(self, request):
#         feeds = Feed.objects.all()
#         serializer = FeedSerializer(feeds, many=True)
#         return Response(serializer.data)


class AllFeeds(APIView):
    def get(self, request):
        all_feeds = Feed.objects.all()
        serializer = FeedSerializer(all_feeds, many=True)
        return Response(serializer.data)


class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound

    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        serializer = FeedDetailSerializer(feed)
        return Response(serializer.data)
