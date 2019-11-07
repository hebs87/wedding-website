from django import forms
from .models import Detail


class DetailForm(forms.ModelForm):
    '''
    Form that allows users to submit their RSVP information
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

    ATTENDING_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No"),
    )

    guest_name = models.ChoiceField(
        label="Your Name Or Group",
        choices=GUEST_CHOICES,
        required=True)
    attending = models.ChoiceField(
        label="Can You Make It?",
        choices=ATTENDING_CHOICES,
        required=True)
    not_attending = models.CharField(
        label="Anyone In Your Group Can't Make It?",
        min_length=2,
        max_length=100,
        widget=forms.TextInput(),
        required=False)
    favourite_song = models.CharField(
        label="Pick A Song For Our Playlist!",
        min_length=2,
        max_length=100,
        widget=forms.TextInput(),
        required=True)
    dietary_requirements = models.CharField(
        label="Any Dietary Requirements?",
        min_length=2,
        max_length=100,
        widget=forms.TextInput(),
        required=False)
    additional_info = models.CharField(
        label="Anything Else We Need To Know?",
        min_length=2,
        max_length=2000,
        widget=forms.Textarea(),
        required=False)
