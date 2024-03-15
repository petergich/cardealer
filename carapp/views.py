from django.shortcuts import render

def home(request):
  return render(request,"index.html")
def cars(request):
  return render(request,"cars.html")
def about(request):
  return render(request,"about.html")
def aboutblog(request):
  return render(request,"blog.html")
def aboutblogdetails(request):
  return render(request,"blog-details.html")
def aboutteam(request):
  return render(request,"team.html")
def abouttestimonials(request):
  return render(request,"testimonials.html")
def aboutfaq(request):
  return render(request,"faq.html")
def aboutterms(request):
  return render(request,"terms.html")
def contact(request):
  return render(request, "contact.html")
def cardetails(request):
  return render(request,"car-details.html")
# Create your views here.
