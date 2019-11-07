from django.shortcuts import render


# Create your views here.
def home(request):
    '''
    Renders home page
    '''
    return render(request, 'index.html')


def location(request):
    '''
    Renders home page
    '''
    return render(request, 'location.html')
