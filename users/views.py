from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .models import User

from rest_framework.views import APIView
from rest_framework.response import Response


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
