from django.contrib import admin
from django.urls import path
from program import views
urlpatterns = [

    path('',views.index,name="index"),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
]
