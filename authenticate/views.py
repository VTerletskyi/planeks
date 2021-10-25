from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from django.contrib.auth import authenticate, login, logout

from loguru import logger


class Login(APIView):

    def post(self, request: Request):
        data = request.data
        logger.info(data)

        user_name = data["username"]
        user_password = data["password"]
        user = authenticate(request, username=user_name, password=user_password)
        if user is not None:
            login(request, user)
            return Response(status="200")
        return Response(status="404")


class Logout(APIView):

    def get(self, request: Request):
        logout(request)
        return Response(status="200")
