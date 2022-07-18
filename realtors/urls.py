from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='realtors'),
    path('<int:listhing_id> ', views.listing, name='listing'),
    path('search/', views.search, name='search'),

]
