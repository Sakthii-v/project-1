from django.shortcuts import render
from .data import articles_data
# Create your views here.

def index(request):
    context={
        'data':articles_data
    }
    return render(request,'new.html',context)

