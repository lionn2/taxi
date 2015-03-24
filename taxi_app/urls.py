from django.conf.urls import url
from taxi_app import views
from taxi_app.views import test, show_map, route_data

urlpatterns = [
	url(r'^$', test),
	url(r'^map/', show_map),
	url(r'^route_data/', route_data)
	#url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]