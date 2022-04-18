from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("만든이 : 강진용")

# Create your views here.
