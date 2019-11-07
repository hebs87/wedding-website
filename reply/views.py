from django.shortcuts import render


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
