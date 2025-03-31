from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
        return HttpResponse ("Helloworld")
def details(request, post_id):
        return HttpResponse(f"This is details page and id is {post_id}")