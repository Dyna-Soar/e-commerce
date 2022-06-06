from django.http import HttpResponse
from products.models import Product


def create_product(request):
    if request.method == 'POST':
        try:
            new_product = Product.objects.create(name=request.POST['name'],
                                                 description=request.POST['description'],
                                                 price=request.POST['price'],
                                                 number_in_store=request.POST['number_in_store'])
            new_product.save()
            return HttpResponse('Product has been created successfully')

        except:
            return HttpResponse('Error in creation')


def update_product(request):
    pass


def increase_number_item(request, product_id, number_add):
    if request.method == 'PUT':
        product = None
        try:
            product = Product.objects.get(id=product_id)
        except:
            return HttpResponse('Error: could not find the product')

        try:
            product.number_in_store += number_add
            product.save()
            return HttpResponse('Number of items has been increased successfully')
        except:
            return HttpResponse('Error: could not increase the number of items')


def decrease_number_item(request, product_id, number_sub):
    if request.method == 'PUT':
        product = None
        try:
            product = Product.objects.get(id=product_id)
        except:
            return HttpResponse('Error: could not find the product')

        try:
            product.number_in_store -= number_sub
            product.save()
            return HttpResponse('Number of items has been decreased successfully')
        except:
            return HttpResponse('Error: could not decrease the number of items')
