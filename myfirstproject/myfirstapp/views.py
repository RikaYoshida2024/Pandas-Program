from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def home(request):
    return render(request,'index.html')

def myfunctionabout(request):
    return HttpResponse("About Response")

def success_page(request):
    print("*"* 10)
    return HttpResponse("<h1>This is a success page.</h1>")