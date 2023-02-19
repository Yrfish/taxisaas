from django.shortcuts import render

#Create your views here.

def homepage_view(request):
    context = {}
    print(request.headers)
    return render(request, "homepage.html", context)
