from django.http import HttpResponse
import json

def hello(request):
    a = {'name': "Hello world !"}
    response = json.dumps(a)
    return HttpResponse(response)
