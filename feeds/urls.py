from django.urls import path
from .views import AllFeeds, FeedDetail, UserFeeds

urlpatterns = [
    path("", AllFeeds.as_view()),
    path("detailFeed/<int:feed_id>", FeedDetail.as_view()),
    path("<str:username>", UserFeeds.as_view()),
]
