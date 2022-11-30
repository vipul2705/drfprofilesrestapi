from django.contrib import admin
from django.urls import path
from profilesproject import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('home/',views.home),
]
