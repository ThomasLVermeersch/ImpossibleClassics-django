from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context = {}
	return render(request, 'home/index.html', context)

def pong(request):
	context = {}
	return render(request, 'home/pong.html', context)

def breakout(request):
	context = {}
	return render(request, 'home/breakout.html', context)

def snake(request):
	context = {}
	return render(request, 'home/snake.html', context)

