from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.rsvp('rsvp', views.RSVPViewSet)

urlpatterns = [
    path('rsvp', include(router.urls)),
    path('location', views.location, name="location"),
    path('rsvp', views.rsvp, name="rsvp"),
    path('admin', views.admin, name="admin"),
]
