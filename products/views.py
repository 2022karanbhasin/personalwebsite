from django.shortcuts import render

# Create your views here.
from .models import Product

def product_Detail_View(request,*args, **kwargs):
        obj = Product.objects.get(id=1)
        context = {
                "object":obj
        }
        return render(request, "product_detail.html",context)
