from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index/index.html")


def about(request):
    return render(request, "index/about.html")

def catalog(request):
    return render(request, "index/catalog.html")


def contacts(request):
    user ={"name" : ["Nurgissa Adilakyn","Elina Afanasyeva"]}
    Email={"email" : ["27681@iitu.edu.kz", "27523@iitu.edu.kz"]}
    position = ("Director-Developer")
    hours = ("9:00-13:00, 14:00-18:00")
    phone = {"phone" : ["77071777777", "77071666666"]}
    data = {"user": user, "email": Email, "hours": hours, "phone": phone,"position":position}
    return render(request, "index/contacts.html", context=data)


def about(request):
    user ={"name" : ["Nurgissa Adilakyn","Elina Afanasyeva"]}
    position = ("Director-Developer")
    age ={"age" : ["20 years","19 years"]}
    location = ("Almaty city")
    data = {"user": user, "position": position, "age": age, "location": location}
    return render(request, "index/about.html", context=data)


