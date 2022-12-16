from django.shortcuts import HttpResponse


def base(reguest):
    return HttpResponse('This is the first page in my site')