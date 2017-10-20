from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request handled by method names 'index'!"
    return HttpResponse(response)

def new(request):
    response = "Hello, I am your next request handled by method names 'new'!"
    return HttpResponse(response)

def create(request):
    response = "Hello, I am your next request handled by method names 'create'!"
    return HttpResponse(response)

def show(request, blog_id):
    response = "Hello, I am your next request handled by method names 'show'!"
    return HttpResponse(response, blog_id)

def edit(request, blog_id):
    response = "Hello, I am your next request handled by method names 'edit'!"
    return HttpResponse(response, blog_id)

def destroy(request, blog_id):
    response = "Hello, I am your next request handled by method names 'destroy'!"
    return HttpResponse(response, blog_id)