from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def learn(request):
    return render(request, 'learn.html')

def map_view(request):
    return render(request, 'map.html')

def report(request):
    return render(request, 'report.html')

def support(request):
    return render(request, 'support.html')

def support(request):
    return render(request, 'roy.html')