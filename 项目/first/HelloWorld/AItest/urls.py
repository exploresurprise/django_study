from django.urls import path
from . import views
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("test1/", views.ai_response, name="number"),
    # path("addmember/", views.add_new_member, name="member"),
]