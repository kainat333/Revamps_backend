# cars/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # This is a simple response; you can render a template instead
    return HttpResponse("Welcome to the Main page!")
def post(self,request):
    return  HttpResponse("This is a post request")
