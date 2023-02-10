from django.http import HttpResponse,request,JsonResponse
from django.shortcuts import render

def home_page(request):
    friends=[
        'shiva',
        'Rakesh',
        'Pandu Rang',
        'Rajiv',
        'Harshit',
        'Harry',
        'Durgesh'
    ]
    print("home page requested")
    # return HttpResponse("<h1>Hello! world</h1>")
    return JsonResponse(friends,safe=False)
