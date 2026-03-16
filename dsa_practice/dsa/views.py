from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def health_check(request):
	return HttpResponse("This project is healthy, I am testing it")
