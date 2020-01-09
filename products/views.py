from django.shortcuts import render

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.

def product_create_view(request):
    form = RawProductForm()
    context = {
        "form": form
    }
    return render (request, "products/product_create.html", context)

#def product_create_view(request):
#    form = ProductForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = ProductForm()
#
#    context = {
#        'form': form
#    }
#    return render (request, "products/product_create.html", context)




def product_detail_view(request):
    obj = Product.objects.get(id=3)
        #context = {
        #    'title': obj.title,
        #    'description': obj.description,
        #    'price': obj.price,
        #}
    context = {
        'object': obj,
    }
    return render (request, "products/product_details.html", context)