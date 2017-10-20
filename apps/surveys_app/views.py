from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request handled by method names 'index'!"
    return HttpResponse(response)

def new(request):
    response = "Hello, I am your next request handled by method names 'new'!"
    return HttpResponse(response)
