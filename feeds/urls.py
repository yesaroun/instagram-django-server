from django.urls import path
from . import views

urlpatterns = [
    path("", views.Feeds.as_view()),
]
