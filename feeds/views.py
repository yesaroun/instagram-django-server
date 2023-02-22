from django.shortcuts import render
from .models import Feed
from rest_framework.views import APIView
from .serializers import FeedSerializer
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
