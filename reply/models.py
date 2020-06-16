from django.db import models


# Create your models here.
# TODO: Add guest list model and have guest_name field in Detail model as FK?
class RSVP(models.Model):
    """
    Allows users to submit their details
    """
    guest_name = models.CharField(
        max_length=27,
        blank=False)
    attending = models.CharField(
        max_length=19,
        blank=False)
    not_attending = models.CharField(
        max_length=100,
        blank=False,
        default="N/A")
    favourite_song = models.CharField(
        max_length=100,
        blank=False)
    favourite_drink = models.CharField(
        max_length=100,
        blank=False,
        default="")
    dietary_requirements = models.CharField(
        max_length=100,
        blank=False,
        default="N/A")
    additional_info = models.TextField(
        max_length=2000,
        blank=False,
        default="N/A")

    class Meta:
        verbose_name = 'RSVP'
        verbose_name_plural = 'RSVPs'

    def __str__(self):
        return "{0} - {1}, {2} can't make it".format(
            self.guest_name, self.attending, self.not_attending)
