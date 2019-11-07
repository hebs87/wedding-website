from django import forms
from .models import Detail


class DetailForm(forms.ModelForm):
    '''
    Form that allows users to submit their RSVP information
    '''
    GUEST_CHOICES = (
        ("Choose an option...", "Choose an option..."),
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
        ("Choose an option...", "Choose an option..."),
        ("Yes", "Yes"),
        ("No", "No"),
    )

    guest_name = forms.ChoiceField(
        label="Your Name Or Group",
        choices=GUEST_CHOICES,
        required=True)
    attending = forms.ChoiceField(
        label="Can You Make It?",
        choices=ATTENDING_CHOICES,
        required=True)
    not_attending = forms.CharField(
        label="Anyone In Your Group Can't Make It?",
        min_length=2,
        max_length=100,
        widget=forms.TextInput(),
        required=False)
    favourite_song = forms.CharField(
        label="Pick A Song For Our Playlist!",
        min_length=2,
        max_length=100,
        widget=forms.TextInput(),
        required=True)
    dietary_requirements = forms.CharField(
        label="Any Dietary Requirements?",
        min_length=2,
        max_length=100,
        widget=forms.TextInput(),
        required=False)
    additional_info = forms.CharField(
        label="Anything Else We Need To Know?",
        min_length=2,
        max_length=2000,
        widget=forms.Textarea(),
        required=False)

    class Meta:
        model = Detail
        fields = [
            "guest_name",
            "attending",
            "not_attending",
            "favourite_song",
            "dietary_requirements",
            "additional_info",
        ]
