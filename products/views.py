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


def view_products(request):
    try:
        products = Product.objects.all()
        return HttpResponse(products)
    except:
        return HttpResponse('Error: could not retrieve products')


def update_product(request):
    pass


def increase_number_item(product_id, increase_item):
    product = None
    try:
        product = Product.objects.get(id=product_id)
    except:
        return 'Error: could not find the product'

    try:
        product.number_in_store += increase_item
        product.save()
        return 'Number of items has been increased successfully'
    except:
        return 'Error: could not increase the number of items'


def decrease_number_item(product_id, decrease_item):
    product = None
    try:
        product = Product.objects.get(id=product_id)
    except:
        return HttpResponse('Error: could not find the product')

    try:
        product.number_in_store -= decrease_item
        product.save()
        return 'Number of items has been decreased successfully'
    except:
        return 'Error: could not decrease the number of items'
