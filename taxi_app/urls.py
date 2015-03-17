from django.conf.urls import url
from taxi_app import views
from taxi_app.views import test

urlpatterns = [
	url(r'^$', test),
	#url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]