# from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')

# def petowner(request):
#     return render(request, 'PetOwner.html')

# def roy(request):
#     return render(request, 'roy.html') 

# def learn(request):
#     return render(request, 'learn.html')

# def map(request):
#     return render(request, 'map.html')

# def report(request):
#     return render(request, 'report.html')

# def support(request):
#     return render(request, 'support.html')

from django.http import HttpResponse
from django.http import JsonResponse

import os

def vue_app(request):
    vue_index_path = os.path.join(os.path.dirname(__file__), 'vue_static', 'index.html')
    with open(vue_index_path, encoding='utf-8') as f:
        return HttpResponse(f.read())

def submit_form(request):
    return HttpResponse("Form submitted successfully!")

def get_data(request):
    data = {
        "message": "This is data from get_data view!"
    }
    return JsonResponse(data)