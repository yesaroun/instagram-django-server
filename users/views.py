from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class MyInfo(APIView):
    def get(self, request):  # Read
        user = request.user

        # Serialize화 해줘야 -> 유저에게 보낼 수 있다.
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def post(self):  # Create
        pass

    def put(self):  # Update
        pass

    # def delete(self):  # Delete
