from django.shortcuts import render, HttpResponse
#from django.shortcuts import HttpResponse
# Create your views here.

def special_case_2003(request):
    return HttpResponse('special case 2003')


def year_archive(request, year):
    return HttpResponse(f'year archive {year}')


def month_archive(request, year, month):
    return HttpResponse(f'month archive {year} - {month}')
