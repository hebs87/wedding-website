from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DetailForm


# Create your views here.
def home(request):
    '''
    Renders home page
    '''
    return render(request, 'index.html')


def location(request):
    '''
    Renders location page
    '''
    return render(request, 'location.html')


def gifts(request):
    '''
    Renders gifts page
    '''
    return render(request, 'gifts.html')


def rsvp(request):
    '''
    Renders rsvp page and allows users to reply
    to the invitation by entering their details
    '''
    if request.method == "POST":
        detail_form = DetailForm(request.POST)
        # Get the guest_name value from the form
        guest_name = request.POST.get("guest_name")
        # Get the attending value from the form
        attending = request.POST.get("attending")
        if detail_form.is_valid():
            # Ensure the guest_name or attending values are valid options
            if guest_name != "Choose an option..."\
              or attending != "Choose an option...":
                detail_form.save()
                # If the user selects 'No' from the attending options
                if attending == "No":
                    messages.success(request, f"Sorry you can't make it :(")
                # If the user doesn't select 'No' from the attending options
                else:
                    messages.success(request, f"Great, see you there :)")
                return redirect(home)
            # If the attending values aren't valid options
            else:
                messages.error(request,
                               "Please select a valid dropdown option")
                return redirect(home)

    else:
        detail_form = DetailForm()

    context = {
        'detail_form': detail_form,
    }

    return render(request, 'rsvp.html', context)
