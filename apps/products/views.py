from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Product
from .forms import AddProductForm
def index(request):
    data = {
        'form':AddProductForm(),
    }
    return render(request, 'products/products.html', data)
def show(request, product_id):
    # user = User.objects.get(id=user_id)
    # context = {
    #     "user" : user,
    # }
    return render(request, 'products/product.html')
def create(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            print 'YAY VALID CREATE'
        else:
            print 'OH HELL NO'

    else:
        form = AddProductForm()
        return redirect(index)
    data = {
        'form':form,
    }
    return render(request, 'products/products.html', data)

    # user = User.objects.get(id=user_id)
    # context = {
    #     "user" : user,
    # }
