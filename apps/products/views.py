from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Product
from .forms import ProductForm
class ProductsView(View):
    #Index Method
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products,
            'form':ProductForm(),
        }
        return render(request, 'products/index.html', context)
    #Create Method
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            print 'YAY VALID CREATE'
            name = request.POST.get("name")
            manufacturer = request.POST.get("manufacturer")
            price = request.POST.get("price")
            description = request.POST.get("description", False)
            product = Product.objects.create(name = name, manufacturer = manufacturer, price = price, description = description)
            return redirect('/products')
        else:
            print 'OH HELL NO'
            products = Product.objects.all()
            context = {
                'products': products,
                'form':form,
            }
            return render(request, 'products/index.html', context)


class ProductView(View):
    #Show Method
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        context = {
            'product':product,
        }
        return render(request, 'products/show.html', context)
    def post(self, request, product_id):
        #Update Method
        if request.POST.get("_method") == 'put':
            print 'in ProductView Post Update'
            form = ProductForm(request.POST)
            if form.is_valid():
                print 'in ProductView Post Update Form Valid'
                name = request.POST.get("name")
                manufacturer = request.POST.get("manufacturer")
                price = request.POST.get("price")
                description = request.POST.get("description", False)
                Product.objects.filter(id=product_id).update(name = name, manufacturer = manufacturer, price = price, description = description)
                return redirect('/products')
            else:
                print 'in ProductView Post Update Form Invalid'
                context = {
                    'form': form,
                }
                return render(request, 'products/edit.html', context)
        #Destroy Method
        else:
            print 'in ProductView Post Delete'
            Product.objects.filter(id=product_id).delete()
            return redirect('/products')

# def index(request):
#     products = Product.objects.all()
#     data = {
#         'products': products,
#         #In Restful this would be in def new
#         'form':AddProductForm(),
#     }
#     return render(request, 'products/index.html', data)
# def product(request, product_id):
#     # user = User.objects.get(id=user_id)
#     # context = {
#     #     "user" : user,
#     # }
#     return render(request, 'products/show.html')
def edit(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(initial={'name':product.name,'manufacturer':product.manufacturer,'price':product.price,'description':product.description})
    context = {
        "form": form,
        "product":product,
    }
    return render(request, 'products/edit.html', context)
# def update(request, product_id):
#     product = Product.objects.get(id=product_id)
#     context = {
#         "product" : product,
#     }
#     return render(request, 'products/edit.html')
# def create(request):
#     if request.method == "POST":
#         form = AddProductForm(request.POST)
#         if form.is_valid():
#             print 'YAY VALID CREATE'
#             name = request.POST.get("name")
#             manufacturer = request.POST.get("manufacturer")
#             price = request.POST.get("price")
#             description = request.POST.get("description", False)
#             product = Product.objects.create(name = name, manufacturer = manufacturer, price = price, description = description)
#             return redirect(index)
#         else:
#             print 'OH HELL NO'
#             context = {
#                 'form':form,
#             }
#             return render(request, 'products/index.html', context)
#
#     else:
#         form = AddProductForm()
#         context = {
#             'form':form,
#         }
#         return render(request, 'products/index.html', context)
# def destroy(request):
#     return redirect(index)
#     # user = User.objects.get(id=user_id)
#     # context = {
#     #     "user" : user,
#     # }
