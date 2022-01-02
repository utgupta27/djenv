from django.http import HttpResponse, response
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("Hello Utsav")

def dynamicPages(request, id):
    return HttpResponse(id)

def homePage(request):
    return render(request, "index.html")

def demoPage(request):
    return render(request, "demoPage.html")

def dynamicDemoPage(request, id):
    data = {
        'title' : id,
    }
    return render(request, "demo.html", data)