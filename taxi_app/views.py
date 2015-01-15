from django.contrib.auth.models import User
from rest_framework import viewsets
from models import *
from serializers import *


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
