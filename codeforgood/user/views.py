from django.shortcuts import render
from . forms import RegistrationForm

from rest_framework.views import APIView
from .serializers import LoginSerializer,  SignUpSerializer
from django.contrib.auth import login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from django.contrib.auth import authenticate         # for Token Authentication
from rest_framework.authtoken.models import Token    # for Token Authentication
from django.views.decorators.csrf import csrf_exempt  # for Token Authentication
from rest_framework.authtoken.views import ObtainAuthToken  # for Token Authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response            # for sending responses
from rest_framework.views import exception_handler

from rest_framework import status
# Create your views here.


def register(request):
	if request.method=="POST":
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form=RegistrationForm()
	context={'form': form}
	return render(request, 'register.html', context)



class LoginViewApp(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "id": user.id})


class SignupView_App(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "id": user.id})
        else:
            return Response(serializer.errors, status=200)
        # return Response({"erreo"})


class LogoutView_App(APIView):

    def post(self, request):
        logout(request)
        return Response(status=204)
