from django.urls import path
from . import views
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("datanumber/", views.return_number, name="number"),
    path("addmember/", views.add_new_member, name="member"),
]



