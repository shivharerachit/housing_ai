from django.contrib import admin
from django.urls import path
from housing_ai import views

urlpatterns = [
    path("", views.index, name='home'),
    path("solution", views.solution, name='solution'),
    # path("services", views.services, name='services') ,        
    # path("contact", views.contact, name='contact'),
]
