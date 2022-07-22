from django.urls import path
from . import views
from ninja import NinjaAPI


#
# @api.get("/add")
# def add(req, a: int, b: int):
#     return {"result": a + b}


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),

]
