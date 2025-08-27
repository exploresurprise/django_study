import json

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .ai_use import models
a = models.get_tongyi_llm()

@require_POST
@csrf_exempt  # 跳过CSRF验证
def ai_response(request):
    print(request)
    text = request.POST.get('question', '')
    answer = a.invoke(text).content
    return_text = json.dumps({'answer':answer})
    return HttpResponse(return_text)
    # pass