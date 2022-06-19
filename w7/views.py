from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Home Page | <a href="/admin">login</a><p><a href="/todo-list-maurosergio">To-do List App</a></p>')