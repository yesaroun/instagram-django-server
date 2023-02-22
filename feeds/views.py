from django.shortcuts import render
from .models import Feed
from rest_framework.views import APIView
from .serializers import FeedSerializer
from rest_framework.response import Response


class Feeds(APIView):
    def get(self, request):
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)
