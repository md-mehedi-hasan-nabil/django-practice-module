from django.shortcuts import render
from django.http import HttpResponse
import http.client
import json
# Create your views here.


def index(request):
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
    conn.request("GET", "/posts")
    response = conn.getresponse()

    data = response.read()
    parsed_data = json.loads(data)

    conn.close()

    context = {"posts": parsed_data}

    return render(request, 'first_app/index.html', context)


def post(request, postId):
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
    conn.request("GET", f"/posts/{postId}")
    response = conn.getresponse()

    data = response.read()
    parsed_data = json.loads(data)

    conn.close()

    context = {"post": parsed_data}

    return render(request, "first_app/post.html", context)


def contact(request):
    return render(request, 'first_app/contact.html')


def about(request):
    return render(request, 'first_app/about.html')
