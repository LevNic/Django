import os
import json

from datetime import datetime

from django.shortcuts import render, get_list_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
from geekshop.settings import BASE_DIR


# Create your views here.


def main(request):
    ''' Главная страница '''
    title = 'главная'

    products_list = Product.objects.all()[:3]

    content = {
        'title': title,
        'products': products_list
    }

    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    '''Страница продукты'''

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category = {'name': 'все'}
        else:
            category = get_list_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(
                category__pk=pk).order_by('-price')
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_list,
            'basket': basket
        }
        return render(request, 'mainapp/products_list.html', content)
    same_products = Product.objects.all()[3:5]
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket
    }
    return render(request, 'mainapp/products.html', content)


def contacts(request):
    '''Страница контакты'''
    title = 'о нас'
    visit_date = datetime.now()
    location = None
    with open(os.path.join(BASE_DIR, 'mainapp/json/contact__locations.json')) as f:
        location = json.load(f)
    content = {'title': title, 'visit_date': visit_date, 'location': location}
    return render(request, 'mainapp/contact.html', content)
