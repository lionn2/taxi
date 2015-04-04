from django.conf.urls import url
from taxi_app import views
from taxi_app.views import *

urlpatterns = [
	url(r'^map/', show_map),
	url(r'^sign_up/', sign_up),
	url(r'^logging/', logging),
	url(r'^logout/', logout),	
	#url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]