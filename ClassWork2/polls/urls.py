from django.urls import path

from . import views

urlpatterns = [
    path('polls/', views.index, name='index'),
    path('hello/<name>', views.hello_name),
    path('times/<int:number>', views.times),
    path('number/<int:number>', views.anumber)
]
