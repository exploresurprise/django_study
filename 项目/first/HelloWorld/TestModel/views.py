from django.shortcuts import render
from django.http import HttpResponse
from .models import Test


# Create your views here.
def return_number(request):
    a = Test.objects
    count = a.count()
    return HttpResponse(f"{count}")
