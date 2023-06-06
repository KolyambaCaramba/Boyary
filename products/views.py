from django.shortcuts import render, get_object_or_404
from math import ceil
from django.http import HttpResponse
from cart.forms import CartAddProductForm
from .models import Category, Product, Podcategory
from django.core.paginator import Paginator


def index(request):
    template = 'products/index.html'
    categorys =    Category.objects.all()
    podcategorys = Podcategory.objects.all()
    
    
    cart_product_form = CartAddProductForm()
    context = {
        'categorys': categorys,
        'podcategorys': podcategorys,
        'cart_product_form': cart_product_form
    }
    return render(request, template, context)

    
        
def category(request, slug):
    template = 'products/category.html'
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    podcategorys = Podcategory.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
         'products': products,
         'category': category,
         'podcategorys': podcategorys,
         'cart_product_form': cart_product_form
     }    
    return render(request, template, context)

def podcategory(request, slug):
    template = 'products/podcategory.html'
    podcategory = get_object_or_404(Podcategory, slug=slug)
    products = Product.objects.filter(podcategory=podcategory)
    cart_product_form = CartAddProductForm()
    context = {
         'products': products,
         'podcategory': podcategory,
         'cart_product_form': cart_product_form,
     
     }
    
    return render(request, template, context)


def product(request,  slug):
    template = 'products/detail.html'
    products = Product.objects.get(slug=slug)
    cart_product_form = CartAddProductForm()
    context = {
         'products': products,
         'cart_product_form': cart_product_form,
         'cart_product_form': cart_product_form
    }   
                                
    return render(request, template, context)






# def index(request):
#     # products = Product.objects.all()
#     # print(products)
#     # n = len(products)
#     # nSlides = n//4 + ceil((n/4)-(n//4))

#     allProds = []
#     catprods = Product.objects.values('category', 'id')
#     cats = {item['category'] for item in catprods}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(prod)
#         nSlides = n // 4 + ceil((n / 4) - (n // 4))
#         allProds.append([prod, range(1, nSlides), nSlides])

#     # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
#     # allProds = [[products, range(1, nSlides), nSlides],
#     #             [products, range(1, nSlides), nSlides]]
#     params = {'allProds':allProds}
#     return render(request, 'products/idex1.html', params)