from django.conf.urls import url
from taxi_app import views

urlpatterns = [
    url(r'^create_client/$', views.create_client),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]