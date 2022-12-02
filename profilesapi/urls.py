from django.urls import path,include
from profilesapi import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello_viewset')

urlpatterns=[
path('hello-view/',views.helloapiview.as_view()),
path('',include(router.urls)),
]
