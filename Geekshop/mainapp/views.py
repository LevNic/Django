import os
import json

from datetime import datetime

from django.shortcuts import render
from geekshop.settings import BASE_DIR
from mainapp.models import Product, ProductCategory

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


def products(request, category_pk=None):
    '''Страница продукты'''
    print(category_pk)
    links_menu = ProductCategory.objects.all()
    content = {
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def contacts(request):
    '''Страница контакты'''
    title = 'о нас'
    visit_date = datetime.now()
    location = None
    with open(os.path.join(BASE_DIR, 'json/contacts.json')) as f:
        location = json.load(f)
    content = {'title': title, 'visit_date': visit_date, 'location': location}
    return render(request, 'mainapp/contact.html', content)
