from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"),
    path('menu.html', views.menu, name='menu'),
    path('about.html', views.about, name='about'),
    path('careers.html', views.careers, name='careers'),
    path('sponsers.html', views.sponsers, name='sponsers'),
    path('contact.html', views.reviewForm, name='reviewForm')
]