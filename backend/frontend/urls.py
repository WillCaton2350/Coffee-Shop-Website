from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.home,
         name='home'),
    path('menu.html',
         views.menu,
         name='menu')
]