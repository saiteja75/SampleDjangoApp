from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path('', views.index, name="Home"),
    path('about', views.about, name="About"),
    path('products', views.products, name="Products"),
    path('carrers', views.carrers, name="Carrers")
]