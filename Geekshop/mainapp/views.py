import os
import json

from datetime import datetime

from django.shortcuts import render
from geekshop.settings import BASE_DIR
from mainapp.models import Product

# Create your views here.
links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'},
]


def main(request):
    title = 'главная'

    products = Product.objects.all()

    content = {
        'title': title,
        'products': products
    }

    return render(request, 'mainapp/index.html', content)


def products(request):

    content = {
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def contacts(request):
    title = 'о нас'
    visit_date = datetime.now()
    location = None
    with open(os.path.join(BASE_DIR, 'json/contacts.json')) as f:
        location = json.load(f)
    content = {'title': title, 'visit_date': visit_date, 'location': location}
    return render(request, 'mainapp/contact.html', content)
