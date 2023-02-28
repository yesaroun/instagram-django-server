import jwt as jwt
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings


class MyInfo(APIView):
    # 로그인한 유저만 허용하겠다. MyInfo 호출을
    permission_classes = [IsAuthenticated]

    def get(self, request):  # Read
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

        # 수업 방식 단 이 방법으로는 하나의 데이터만 받아와짐
        # user = request.user       # 이러면 python이 알아서 찾아주는 듯
        #
        # # Serialize화 해줘야 -> 유저에게 보낼 수 있다.
        # serializer = UserSerializer(user)
        #
        # return Response(serializer.data)

    def post(self):  # Create
        pass

    def put(self):  # Update
        pass

    # def delete(self):  # Delete


class Login(APIView):
    """django의 seesion을 활용한 로그인"""

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError()

        user = authenticate(
            request,
            username=username,
            password=password,
        )
        print(user)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class Logout(APIView):
    """django의 session을 활용한 로그아웃"""

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class JWTLogin(APIView):
    """jwt를 통한 로그인 처리"""

    def post(self, request):
        username = request.data.gate("username")
        password = request.data.gate("password")

        if not username or not password:
            raise ParseError

        user = authenticate(request, username=username, password=password)

        # 토큰을 만드는 키
        if user:
            token = jwt.encode(
                {"id": user.id, "username": user.username},
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            print("token: " + token)
            return Response({"token": token})
