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

def dataPage(request):
    data = {
        'title' : "Students List",
        'students' : [
            {'name' : 'Utsav Gupta' , 'section' : 'CS41', 'branch' : 'CSE', 'course' : 'B.Tech.'},
            {'name' : 'Suhal Kumar' , 'section' : 'CS41', 'branch' : 'CSE', 'course' : 'B.Tech.'},
            {'name' : 'Amaresh Tiwari' , 'section' : 'CS41', 'branch' : 'CSE', 'course' : 'B.Tech.'},
            {'name' : 'Anmol Srivastava' , 'section' : 'CS41', 'branch' : 'CSE', 'course' : 'B.Tech.'},
            {'name' : 'Shubham Singh' , 'section' : 'CS41', 'branch' : 'CSE', 'course' : 'B.Tech.'},
            {'name' : 'Shubham Yadav' , 'section' : 'CS41', 'branch' : 'CSE', 'course' : 'B.Tech.'},
            {'name' : 'Sunil Gupta' , 'section' : 'CS41', 'branch' : 'CSE', 'course' : 'B.Tech.'},
            {'name' : 'Vipin Kumar Yadav' , 'section' : 'CS41', 'branch' : 'CSE', 'course' : 'B.Tech.'},
            {'name' : 'Som Shiv Gupta' , 'section' : 'CS41', 'branch' : 'CSE', 'course' : 'B.Tech.'},
            {'name' : 'Shyam Ji Shukla' , 'section' : 'CS41', 'branch' : 'CSE', 'course' : 'B.Tech.'},
            {'name' : 'Ved Prakash Singh' , 'section' : 'CS41', 'branch' : 'CSE', 'course' : 'B.Tech.'},
        ]
    }
    return render(request, "data.html", data)