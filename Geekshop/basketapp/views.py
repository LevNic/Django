from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket

# Create your views here.


def basket(request):
    connent = {

    }
    return render(request, '', content)


def basket_add(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(
        product=product_item, user=request.user).first()

    if not basket_item:
        basket_item = Basket.objects.create(
            product=product_item, user=request.user)

    basket_item.quantity += 1
    basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    content = {

    }
    return render(request, '', content)
