from rest_framework import serializers
from django.contrib.auth import authenticate         # for Token Authentication
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token    # for Token Authentication
from rest_framework.response import Response            # for sending responses

from rest_framework import exceptions

from . import models


class LoginSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""

    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, data):
        """Validate and authenticate the user"""
        username = data.get('username', ""),
        password = data.get("password")

        if username and password:
            user = authenticate(username=username[0], password=password)
            if user:
                data["user"] = user

            else:
                msg = "Unable to login with given Password"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, data):
        """Validate and authenticate the user"""
        username = data.get('username', ""),
        password = data.get("password")
        if username and password:
            instance = User.objects.filter(username=username[0])
            if instance:
                msg = "Username already exist !"
                print("exists")
                raise exceptions.ValidationError(msg)

            else:

                User.objects.create_user(
                    username[0], email=None, password=password)
                user = authenticate(username=username[0], password=password)
                if user:
                    data["user"] = user
                else:
                    msg = "Unable to login with given credentials"
                    raise exceptions.ValidationError(msg)
                return data
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
