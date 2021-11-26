from django.shortcuts import render
from django.http import HttpResponse
from .models import Cakes




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
    age ={"age" : ["20 years","20 years"]}
    location = ("Almaty city")
    data = {"user": user, "position": position, "age": age, "location": location}
    return render(request, "index/about.html", context=data)


def index(request):
    title = 'CATALOG'
    category1 = {'image': 'static/images/birth-cakes.jpg', 'name': 'birthday cakes',
                 'description': 'Please your loved ones with a masterpiece of cooking', 'ssylka': 'birthday', 'ssylka1': 'birthday'}
    category2 = {'image': 'static/images/wedding-cakes.jpeg', 'name': 'Wedding cakes',
                 'description': 'Please your loved ones with a masterpiece of cooking', 'ssylka': 'wedding', 'ssylka1': 'wedding'}
    category3 = {'image': 'static/images/kids-cakes.jpeg', 'name': 'kids cakes',
                 'description': 'Please your loved ones with a masterpiece of cooking', 'ssylka': 'kids', 'ssylka1': 'kids'}
    category4 = {'image': 'static/images/corporative-cakes.jpeg', 'name': 'Corporative cakes',
                 'description': 'Please your loved ones with a masterpiece of cooking', 'ssylka': 'corporative', 'ssylka1': 'corporative'}
    category5 = {'image': 'static/images/aesthetic-cakes.jpeg', 'name': 'Aesthetic cakes',
                 'description': 'Please your loved ones with a masterpiece of cooking', 'ssylka': 'aesthetic', 'ssylka1': 'aesthetic'}
    categories = [category1, category2, category3, category4, category5]
    dataToHtml = {'title': title, 'categories': categories}
    return render(request, "index/index.html", context=dataToHtml)


# def article_list(request):
#     context = {"articles": Articles.objects.all()}
#     return render(request, "list.html", context)


def aesthetic(request):
    title = 'Aesthetic'
    aesthetics = Cakes.objects.filter(category='Aesthetic')
    dataToHtml = {'title': title, 'aesthetics': aesthetics}
    return render(request, "index/aesthetic.html", context=dataToHtml)


def birthday(request):
    title = 'Birthday'
    birthdays = Cakes.objects.filter(category='Birthday')
    dataToHtml = {'title': title, 'birthdays': birthdays}
    return render(request, "index/birthday.html", context=dataToHtml)


def kids(request):
    title = 'Kids'
    kidss = Cakes.objects.filter(category='Kids')
    dataToHtml = {'title': title, 'kidss': kidss}
    return render(request, "index/kids.html", context=dataToHtml)


def wedding(request):
    title = 'Wedding'
    weddings = Cakes.objects.filter(category='Wedding')
    dataToHtml = {'title': title, 'weddings': weddings}
    return render(request, "index/wedding.html", context=dataToHtml)


def corporative(request):
    title = 'Corporative'
    corp = Cakes.objects.filter(category='Corporative')
    dataToHtml = {'title': title, 'corp': corp}
    return render(request, "index/corporative.html", context=dataToHtml)



