from django.contrib.auth.models import User
from rest_framework import viewsets
from models import *
from serializers import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

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


#reistration of client
def create_client(request):
	try:
		username = request.POST['username']
	except:
		return HttpResponse('result:invalid username')
	try:
		user = User.objects.get(username = username)
		return HttpResponse('result:username is busy')
	except:	
		try:
			email = request.POST['email']
		except:
			return HttpResponse('result:invalid email')
		try:
			password = request.POST['password']
		except:
			return HttpResponse('result:invalid password')	
		try:
			client = ClientUser.objects.create_user(username, email, password
				#'user1', 'andriy@qw.ua', 'user1'
				)
		except:	
			return HttpResponse('result:exception')
		try: 
			client.rating = request.POST['rating']
		except: 
			return HttpResponse('result:invalid rating')
		try:
			client.photo = request.FILES['photo']
		except:
			return HttpResponse('result:invalid photo')
		client.date_registration = datetime.datetime.now()
		client.save()
		serializer = ClientUserSerializer(client)
		return JSONResponse(serializer.data)


#reistration of driver
def create_driver(request):
	try:
		username = request.POST['username']
	except:
		return HttpResponse('result:invalid username')
	try:
		user = User.objects.get(username = username)
		return HttpResponse('result:username is busy')
	except:	
		try:
			email = request.POST['email']
		except:
			return HttpResponse('result:invalid email')
		try:
			password = request.POST['password']
		except:
			return HttpResponse('result:invalid password')	
		try:
			driver = DriverUser.objects.create_user(username, email, password)
		except:
			return HttpResponse('result:exception')
		try:
			driver.photo_car = request.FILES['photo_car']
		except:
			return HttpResponse('result:invalid photo_car')
		try:
			driver.photo_driver_license = request.FILES['photo_driver_license']
		except:
			return HttpResponse('result:invalid photo_driver_license')
		try:
			driver.photo_car_license = request.FILES['photo_car_license']
		except:
			return HttpResponse('result:invalid photo_car_license')
		try:
			driver.rate_min = request.POST['rate_min']
		except:
			return HttpResponse('result:invalid rate_min')
		try:
			driver.rate_km_hightway = request.POST['rate_km_hightway']
		except:
			return HttpResponse('result:invalid rate_km_hightway')
		try:
			driver.rate_km_city = request.POST['rate_km_city']
		except:
			return HttpResponse('result:invalid rate_km_city')
		try:
			driver.about_me = request.POST['about_me']
		except:
			return HttpResponse('result:invalid about_me')
		try:
			driver.coefficient_congestion = request.POST['coefficient_congestion']
		except:
			return HttpResponse('result:invalid coefficient_congestion')
		driver.state = 2
		try:
			location = Location(x = request.POST['x'], y = request.POST['y'])
		except:
			return HttpResponse('result:invalid location')
		driver.location = location
		driver.save()
		serializer = DriverUser(driver)
		return JSONResponse(serializer.data)