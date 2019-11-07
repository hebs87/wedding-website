from django.db import models


# Create your models here.
class Guest(models.Model):
    '''
    Provides the choices for the guest names
    '''
    GUEST_CHOICES = (
        ("Ash and Saf", "Ash and Saf"),
        ("Becky and Stu", "Becky and Stu"),
        ("Brittany and Jake", "Brittany and Jake"),
        ("Bunty", "Bunty"),
        ("Charlotte and Sean", "Charlotte and Sean"),
        ("Gary, Vicki and Callum", "Gary, Vicki and Callum"),
        ("Giri and Gill", "Giri and Gill"),
        ("Indira", "Indira"),
        ("Jack (Best Man)", "Jack (Best Man)"),
        ("Jack, Toni and Archie", "Jack, Toni and Archie"),
        ("Jimmy and Iris", "Jimmy and Iris"),
        ("Josh, Amy, Oscar and Archie", "Josh, Amy, Oscar and Archie"),
        ("Lee and Will", "Lee and Will"),
        ("Lisa and David", "Lisa and David"),
        ("Paul and Tracey", "Paul and Tracey"),
        ("Rach, Ste, Bobby and Sam", "Rach, Ste, Bobby and Sam"),
    )

    guest_name = models.CharField(
        max_length=27,
        unique=True,
        choices=GUEST_CHOICES)

    def __str__(self):
        return self.guest_name


class Attending(models.Model):
    '''
    Provides a Yes/No choice for whether guests
    are attending
    '''
    ATTENDING_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No"),
    )

    attending = models.CharField(
        max_length=3,
        unique=True,
        choices=GUEST_CHOICES)

    def __str__(self):
        return self.attending
