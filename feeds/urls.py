from django.urls import path
from .views import AllFeeds, FeedDetail

urlpatterns = [
    path("", AllFeeds.as_view()),
    path("<int:feed_id>", FeedDetail.as_view()),
]
