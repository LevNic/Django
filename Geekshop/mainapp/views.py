from django.shortcuts import render

# Create your views here.
links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'},
]


def main(request):
    content = {

    }

    return render(request, 'mainapp/index.html', content)


def products(request):

    content = {
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def contacts(request):
    return render(request, 'mainapp/contact.html')
