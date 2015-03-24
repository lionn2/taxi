from django.contrib.auth.models import User
from rest_framework import viewsets
from models import *
from serializers import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render

import datetime


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class ClientUserViewSet(viewsets.ModelViewSet):
	queryset = ClientUser.objects.all()
	serializer_class = ClientUserSerializer


class DriverUserViewSet(viewsets.ModelViewSet):
	queryset = DriverUser.objects.all()
	serializer_class = DriverUserSerializer


class LocationViewSet(viewsets.ModelViewSet):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer


class StatisticViewSet(viewsets.ModelViewSet):
	queryset = Statistic.objects.all()
	serializer_class = StatisticSerializer


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


class DriverRatingViewSet(viewsets.ModelViewSet):
	queryset = DriverRating.objects.all()
	serializer_class = DriverRatingSerializer


class ClientRatingViewSet(viewsets.ModelViewSet):
	queryset = ClientRating.objects.all()
	serializer_class = ClientRatingSerializer


class CommentsViewSet(viewsets.ModelViewSet):
	queryset = Comments.objects.all()
	serializer_class = CommentsSerializer

def test(request):
	return render(request, 'index.html')

def show_map(request):
	return render(request, 'map.html')

def route_data(request):
	return HttpResponse("ok")

def sign_up(request):
	return render(request, 'Signup.html')