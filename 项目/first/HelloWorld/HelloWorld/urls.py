"""
URL configuration for HelloWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from . import views, testdb
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("first/", views.hello, name="hello"),
    # path("", views.hello, name="hello"),
    # path('runoob/', views.runoob),
    # path('testdb/', testdb.testdb),
    path('AItest/',include('AItest.urls')),
    path('testmodel/',include('TestModel.urls'))
]
# path()函数参数作用
# path(route, view, kwargs=None, name=None)
# route： 字符串，定义 URL 的路径部分。可以包含变量，例如 <int:my_variable>，以从 URL 中捕获参数并将其传递给视图函数。
#
# view： 视图函数，处理与给定路由匹配的请求。可以是一个函数或一个基于类的视图。
#
# kwargs（可选）： 一个字典，包含传递给视图函数的额外关键字参数。
#
# name（可选）： 为 URL 路由指定一个唯一的名称，以便在代码的其他地方引用它。这对于在模板中生成 URL 或在代码中进行重定向等操作非常有用。

