from django.shortcuts import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from shop.models import Product, OrderHeader, OrderLine
import json

def products(request):
    if ('page_no' in request.GET) and ('page_size' in request.GET):
        products = Product.objects.all()
        paginator = Paginator(products, request.GET['page_size'])
        return HttpResponse(serializers.serialize('json', paginator.page(request.GET['page_no'])))
    else:
        return HttpResponse("Usage: http://ipaddress:8000/shop/api/product?page_no=x&page_size=y")

def orders(request):
    if ('page_no' in request.GET) and ('page_size' in request.GET):
        orders = OrderLine.objects.all()
        paginator = Paginator(orders, request.GET['page_size'])
        return HttpResponse(serializers.serialize('json', paginator.page(request.GET['page_no'])))
    else:
        return HttpResponse("Usage: http://ipaddress:8000/shop/api/orders?page_no=x&page_size=y")

def related_products(request):
    if ('id' in request.GET) :
        rel_prods = {}
        orders = OrderHeader.objects.all()
        for order in orders:
            lines = OrderLine.objects.filter(order_id=order.id, product_id=request.GET['id'])
            if lines.count() > 0:
                rel_lines = OrderLine.objects.filter(order_id=order.id).exclude(product_id=request.GET['id'])
                if rel_lines.count() > 0:
                    for rel_line in rel_lines:
                        if rel_line.product_id in rel_prods.keys():
                            rel_prods[rel_line.product_id] = rel_prods.get(rel_line.product_id) + 1
                        else:
                            rel_prods[rel_line.product_id] = 1
        sorted_rel_prod_list = sorted(rel_prods.items(),key=lambda item: item[1], reverse=True)
        output_list = []
        for prod in sorted_rel_prod_list:
            rel_prod = Product.objects.get(id=prod[0])
            output_list.append({'id': rel_prod.id, 'name': rel_prod.name, 'sales_orders': prod[1]})
        return HttpResponse(json.dumps(output_list))
    else:
        return HttpResponse("Usage: http://ipaddress:8000/shop/api/related_products?id=x")
