from django.conf.urls import url
from taxi_app import views

urlpatterns = [
    url(r'^create_client/$', views.create_client),
	url(r'^create_driver/$', views.create_driver),
	url(r'^get_set_location/(?P<pk>[0-9]+)/$', views.get_set_location),
	#url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]