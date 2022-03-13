from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    context = {}
    return render(request, 'home/index.html', context)
