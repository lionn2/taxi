from django.contrib.auth.models import User
from models import *
from rest_framework import serializers
import md5

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 
        	'username', 
        	'password', 
        	'email'
        	)


class ClientUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ClientUser
		fields = ('url',
			'username',
			'email',
			'password',
			'rating',
			'photo',
			'date_registration'
			)

	def create(self, validated_data):
	 	print validated_data
	 	validated_data['password'] = md5.md5(validated_data['password']).hexdigest()
	 	return ClientUser.objects.create(**validated_data)



class DriverUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DriverUser
		fields = ('url', 
			'username', 
			'password',
			'email', 'photo_car', 
			'photo_driver_license', 
			'photo_car_license', 
			'rate_min', 
			'rate_km_hightway', 
			'rate_km_city', 
			'about_me',
			'coefficient_congestion',
			'state',
			'location',
			'rating'
		)


class LocationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Location
		fields = ('url', 
			'id',
			'x',
			'y',
			'city',
			'street',
			'building'
			)


class StatisticSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Statistic
		fields = ('url', 
			'id',
			'count_orders',
			'count_drivings',
			'on_app',
			'user'
			)


class ClientRatingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ClientRating
		fields = ('url', 
			'id',
			'value',
			'driver',
			'client'
			)


class DriverRatingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DriverRating
		fields = ('url', 
			'id',
			'car_state',
			'order_execution',
			'comfort',
			'driver',
			'client',
			'avarage_value'
			)


class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Order
		fields = ('url', 
			'id',
			'date',
			'cost',
			'start_location',
			'end_location',
			'client_rating',
			'driver_rating',
			'state',
			'time_travel',
			'long_travel',
			'is_fast',
			'driver',
			'client'
			)


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comments
		fields = ('url', 
			'id',
			'date',
			'whom',
			'order',
			'driver',
			'client'
			)