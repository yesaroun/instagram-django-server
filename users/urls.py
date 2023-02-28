from django.urls import path
from .views import MyInfo, Login, Logout

urlpatterns = [
    path("myinfo/", MyInfo.as_view()),
    path("login", Login.as_view()),
    path("logout", Logout.as_view()),
]
