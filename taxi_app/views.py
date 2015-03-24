from django.contrib.auth.models import User
from rest_framework import viewsets
from models import *
from serializers import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
import md5
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

def show_map(request):
	return render(request, 'map.html')

def sign_up(request):
	return render(request, 'Signup.html')

def logging(request):
	username = request.POST['username']
	try:
		user = User.objects.get(username = username)
		password = md5.md5(request.POST['password']).hexdigest()
		if user.password == password:
			user.is_authorized = True
			user.save()
			return HttpResponse("ok")
		
		else:
			return HttpResponse("fail")
	except:
		return HttpResponse("fail")

def logout(request):
	try:
		user = User.objects.get(username = request.POST['username'])
		user.is_authorized = False
		user.save()
		return HttpResponse("ok")	
	except:
		return HttpResponse("fail")