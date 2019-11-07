from django.db import models


# Create your models here.
class Detail(model.Model):
    '''
    Allows users to submit their details
    '''
    guest_name = models.CharField(
        max_length=27,
        blank=False)
    attending = models.CharField(
        max_length=3,
        blank=False)
    not_attending = models.CharField(
        max_length=100,
        blank=False)
    favourite_song = models.CharField(
        max_length=100,
        blank=False)
    dietary_requirements = models.CharField(
        max_length=100,
        blank=False)
    additional_info = models.TextField(
        max_length=2000,
        blank=False)
