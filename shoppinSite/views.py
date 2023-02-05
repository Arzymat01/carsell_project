from django.shortcuts import render

# Create your views here.
def  index(request):
    return render(request,'shoppinSite/index.html')


def about(request):
    return render(request,'shoppinSite/about.html')


def contact(request):
    return render(request, 'shoppinSite/contact.html')


def productsdescription(request):
    return render(request, 'shoppinSite/productsdescription.html')


def skida(request):
    return render(request, 'shoppinSite/skida.html')


