from django.urls import path

from blog02 import views

urlpatterns = [
    path('', views.hello),
    path('index/', views.index, name='index'),
    path('method01/', views.method01),
]