from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def hello_name(request, name):
    return HttpResponse('Hello ' + name)


def times(request, number):
        return HttpResponse(('Your number times 2 is: ', 2 * number))


def anumber(request, number):
    for x in range(0, number):
        print(x)
    return HttpResponse(('SUM is: ', number))