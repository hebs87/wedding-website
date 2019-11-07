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
        blank=False,
        default="N/A")
    favourite_song = models.CharField(
        max_length=100,
        blank=False)
    dietary_requirements = models.CharField(
        max_length=100,
        blank=False,
        default="N/A")
    additional_info = models.TextField(
        max_length=2000,
        blank=False,
        default="N/A")

    def __str__(self):
        return "{0} - {1}, {2} can't make it".format(
            self.guest_name, self.attending, self.not_attending)
