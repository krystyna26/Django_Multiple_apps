from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request, ):
    response = "register!"
    return HttpResponse(response)

def login(request):
    response = "login"
    return HttpResponse(response)
    
def allUsers(request):
    response = "list of all users"
    return HttpResponse(response)