from django.shortcuts import render
from .models import Species
import json

def home(request):
    species_list = Species.objects.all()
    species_json = list(species_list.values('name_common', 'name_scientific', 'status', 'species_subgroup'))
    return render(request, 'home.html', {
        'species_list': species_list,
        'species_json': json.dumps(species_json),
    })

def petowner(request):
    return render(request, 'PetOwner.html')

def roy(request):
    return render(request, 'roy.html')

def learn(request):
    return render(request, 'learn.html')

def map(request):
    return render(request, 'map.html')

def report(request):
    return render(request, 'report.html')

def support(request):
    return render(request, 'support.html')

