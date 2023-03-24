from django.shortcuts import render

def home(request):
    return render(request, 'digital_design_app/home.html')
