from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logreg/', views.logreg, name='logreg'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('details/', views.details, name='details'),
    path('sitters/', views.sitters, name='sitters'),
    path('book/', views.book, name='book'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
