from django.urls import path
from . import views

urlpatterns = [
    path('location', views.location, name="location"),
    path('rsvp', views.rsvp, name="rsvp"),
    path('admin', views.admin, name="admin"),
]
