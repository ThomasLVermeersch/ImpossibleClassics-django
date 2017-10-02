from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^pong/', views.pong, name='pong'),
	url(r'^breakout/', views.breakout, name='breakout'),
	url(r'^snake/', views.snake, name='snake'),
]