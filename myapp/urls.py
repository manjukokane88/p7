from django.http import HttpResponse
from django.urls import path
from myapp import views



urlpatterns = [

    path('child',views.child,name='child'),
    path('demo',views.demo,name='demo'),
]

