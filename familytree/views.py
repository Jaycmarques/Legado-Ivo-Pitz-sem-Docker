from django.shortcuts import render

# Create your views here.


def familytree(request):
    # Your view logic for the index page
    return render(request, 'familytree/index.html')


def detail(request):
    # Your view logic for the detail page
    return render(request, 'familytree/familymember.html')
