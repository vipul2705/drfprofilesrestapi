from django.contrib import admin
from django.urls import path,include
from profilesproject import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('home/',views.home),
    path('api/',include('profilesapi.urls')),
]
