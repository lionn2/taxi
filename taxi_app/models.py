from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
	x = models.FloatField()
	y = models.FloatField()
	city = models.CharField(max_length = 50)
	street = models.CharField(max_length = 50)
	building = models.CharField(max_length = 5)


class DriverUser(User):
	photo_car = models.ImageField(blank = True)
	photo_driver_license = models.ImageField(blank = True)
	photo_car_license = models.ImageField(blank = True)
	rate_min = models.IntegerField()
	rate_km_hightway = models.IntegerField()
	rate_km_city = models.IntegerField()
	about_me = models.TextField()
	coefficient_congestion = models.FloatField(default = 1)
	state = models.IntegerField()
	location = models.OneToOneField(Location)
	rating = models.IntegerField(default = 0)


class ClientUser(User):
	rating = models.FloatField()
	photo = models.ImageField(blank = True)
	date_registration = models.DateTimeField(auto_now_add=True)
	favourite_drivers = models.ManyToManyField(DriverUser)


class Statistic(models.Model):
	count_orders = models.IntegerField()
	count_drivings = models.IntegerField()
	on_app = models.IntegerField()			#how many you was enter to app
	user = models.OneToOneField(User)


class ClientRating(models.Model):
	value = models.IntegerField()
	driver = models.ForeignKey(DriverUser)
	client = models.ForeignKey(ClientUser)


class DriverRating(models.Model):
	car_state = models.IntegerField()
	order_execution = models.IntegerField()
	comfort = models.IntegerField()
	client = models.ForeignKey(ClientUser)
	driver = models.ForeignKey(DriverUser)
	avarage_value = models.FloatField()


class Order(models.Model):
	date = models.DateTimeField()
	cost = models.FloatField()
	start_location = models.OneToOneField(Location, related_name = 'start_location')
	end_location = models.OneToOneField(Location, related_name = 'end_location')
	client_rating = models.OneToOneField(ClientRating)
	driver_rating = models.OneToOneField(DriverRating)
	state = models.IntegerField()
	time_travel = models.IntegerField()
	long_travel = models.IntegerField()
	is_fast = models.BooleanField(default = True)
	driver = models.ForeignKey(DriverUser)
	client = models.ForeignKey(ClientUser)


class Comments(models.Model):
	client = models.ForeignKey(ClientUser)
	driver = models.ForeignKey(DriverUser)
	whom = models.IntegerField()
	date = models.DateTimeField(auto_now_add = True)
	order = models.ForeignKey(Order)