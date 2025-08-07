import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Test


# Create your views here.
def return_number(request):  # 返回数据库行数
    a = Test.objects
    count = a.count()
    return HttpResponse(f"{count}")


@csrf_exempt
def add_new_member(request):
    if not request.body:
        return HttpResponse(json.dumps({'name': '无body'}))
    a = json.loads(request.body)

    name = a['name']
    b = Test()
    b.name = name
    b.save()
    return HttpResponse(json.dumps({'name': '添加成功'}))
