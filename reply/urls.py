from django.urls import path, include
from .views import location, gifts, rsvp

urlpatterns = [
    path('location', location, name="location"),
    path('gifts', gifts, name="gifts"),
    path('rsvp', rsvp, name="rsvp"),
]
