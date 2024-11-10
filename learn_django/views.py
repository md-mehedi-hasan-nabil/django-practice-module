from django.http import HttpResponse

def contact(request):
    return HttpResponse("Contact page")


def home(request):
    return HttpResponse("Home page")