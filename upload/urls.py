from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name='main'),
	url(r'^image/(?P<pk>[0-9]+)/$', views.image_detail, name='image_detail'),
]