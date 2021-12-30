from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('about/', views.about),
    path('contactus/', views.contactus),
    path('donate/',views.donates),
    path('login/',views.login),
    path('membership/',views.memberships),
    path('event/',views.event),
    path('gallery/',views.imagegallery),
    path('videogallery/',views.videogallery),
    path('privacy/',views.privacy),
    path('termsconditions/',views.Terms),
]
