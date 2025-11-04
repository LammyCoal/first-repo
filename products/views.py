from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product


def index(request):
    product = Product.objects.all()
    return render(request,'index.html',{'products':product} )

def new(request):
    return HttpResponse("This is the news page!!")
