from django.urls import path
from . import views
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("datanumber/", views.return_number, name="number"),

]



