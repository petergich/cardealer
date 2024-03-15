from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("cars",views.cars,name="cars"),
    path("about",views.about,name="about"),
    path("blog",views.aboutblog,name="blog"),
    path("blogdetails",views.aboutblogdetails,name="blogdetails"),
    path("team",views.aboutteam,name="team"),
    path("testimonials",views.abouttestimonials,name="testimonials"),
    path("faq",views.aboutfaq,name="faq"),
    path("terms",views.aboutterms,name="terms"),
    path("contact",views.contact,name="contact"),
    path("cardetais",views.cardetails,name="cardetails"),
]

