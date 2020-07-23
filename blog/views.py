from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from .models import User
import json


def bd(request):
    user_list = str(list(User.objects.all())).replace("'", '"')
    user_list = json.loads(user_list)
    return JsonResponse({"result": user_list})


def write(request):
    r = User(username="Саня")
    r.save()
    return JsonResponse({"result": 200})


def sparta(request):
    return JsonResponse({"message": "Hello Sparta"})
