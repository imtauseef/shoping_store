from django.shortcuts import render
from .models import Product, Order
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    allProducts = Product.objects.all()

    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        allProducts = Product.objects.filter(title__icontains=item_name)

    #pagination
    pagination = Paginator(allProducts, 4)
    select_page = request.GET.get('page')
    allProducts = pagination.get_page(select_page)
    
    context = {
        'all_products': allProducts,
    }
    return render(request, 'shoping_app/home.html', context)


def detail(request, pk):
    productName = Product.objects.get(id=pk)

    context = {
        'product_name': productName,
    }
    return render(request, 'shoping_app/detail.html', context)


def checkout(request):
    if request.method == "POST":
        items = request.POST.get("items", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zipcode = request.POST.get("zip", "")
        totalPrice = request.POST.get("totalprice", "")

        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, totalprice=totalPrice)
        order.save()

    context = {}
    return render(request, 'shoping_app/checkout.html', context)