from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def petowner(request):
    return render(request, 'PetOwner.html')


def roy(request):
    return render(request, 'roy.html')