from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Hello Utsav")

def dynamicPages(request, id):
    return HttpResponse(id)
