from django.shortcuts import render

def home(request):
  return render(request,"cars.html")
# Create your views here.
