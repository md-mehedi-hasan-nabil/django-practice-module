from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:postId>/', views.post, name='post'),
    path('about', views.about, name='about'),
    path('contact-us', views.contact, name='contact-us'),
]
