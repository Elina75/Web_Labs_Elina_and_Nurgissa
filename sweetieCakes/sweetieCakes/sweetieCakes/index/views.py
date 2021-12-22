from django.shortcuts import render, redirect
from .models import Cakes
from .forms import ProductForm
from django.views.generic.edit import UpdateView, DeleteView




def registration(request):
    return render(request, "index/registration.html")


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
    aesthetics = Cakes.objects.filter(category=1)
    dataToHtml = {'title': title, 'aesthetics': aesthetics}
    return render(request, "index/aesthetic.html", context=dataToHtml)


def birthday(request):
    title = 'Birthday'
    ssylka1 = {'birthdayProduct1'}
    ssylki = [ssylka1]
    birthdays = Cakes.objects.filter(category=2)
    dataToHtml = {'title': title, 'birthdays': birthdays, 'ssylki': ssylki}
    return render(request, "index/birthday.html", context=dataToHtml)


def wedding(request):
    title = 'Wedding'
    weddings = Cakes.objects.filter(category=3)
    dataToHtml = {'title': title, 'weddings': weddings}
    return render(request, "index/wedding.html", context=dataToHtml)


def kids(request):
    title = 'Kids'
    kidss = Cakes.objects.filter(category=4)
    dataToHtml = {'title': title, 'kidss': kidss}
    return render(request, "index/kids.html", context=dataToHtml)


def corporative(request):
    title = 'Corporative'
    corp = Cakes.objects.filter(category=5)
    dataToHtml = {'title': title, 'corp': corp}
    return render(request, "index/corporative.html", context=dataToHtml)


def productdetailbuy(request, id):
    title = 'product'
    product = Cakes.objects.get(id=id)
    return render(request, "index/productdetailbuy.html", {'product': product, 'title': title})


def products(request):
    products = Cakes.objects.all()
    dataToHtml = {'products': products}
    return render(request, 'index/products.html', context=dataToHtml)


def createproduct(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('productspage')
    return render(request, 'index/createproduct.html', {'form': form})


def product(request, id):
    product = Cakes.objects.get(id=id)
    return render(request, 'index/productdetails.html', {'product': product})


class productupdate(UpdateView):
    model = Cakes
    fields = '__all__'
    success_url = '/all-products'


class productdelete(DeleteView):
    model = Cakes
    success_url = '/all-products'