from django.shortcuts import render

# Create your views here.


def homepage(request):
    context = {}
    return render(request, "core/index.html", context)

def aboutpage(request):
    context = {}
    return render(request, "core/about.html", context)

def productpage(request):
    context = {}
    return render(request, "core/product.html", context)

def bloggpage(request):
    context = {}
    return render(request, "core/blogg.html", context)

def contactuspage(request):
    context = {}
    return render(request, "core/contactus.html", context)