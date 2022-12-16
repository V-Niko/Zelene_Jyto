from django.shortcuts import render, HttpResponse
#from django.shortcuts import HttpResponse
# Create your views here.

def add(request):
    return HttpResponse('manager add')


def delete(request):
    return HttpResponse('manager delete')


def edit(request):
    return HttpResponse('manager edit')
