from django.db.models.fields import IntegerField
from django.shortcuts import render
from website_app.models import Products
from django.shortcuts import render,  HttpResponseRedirect, redirect
from django import forms
from website_app import views
import locale


# Create your views here.
def index_view(request):
    product = Products.objects.all()
    first_product = product[0]
    print(first_product.product_image)
    return render(request,'index.html',{'product':product})

# This is an attempt at converting the given int into currency format
# def number_to_price(request):
#     number_string = ''
#     number_commas_only = "{:,}".format(number_string)
#     number_two_decimal = "{:.2f}".format(number_string)
#     currency_string = "${:,.2f}".format(number_string)
#     return render(request.currency_string)

class AddProductsForm(forms.ModelForm):
    class Meta:
        model= Products
        fields= ('tagline','description','product_image','category')
        price= int('500', 0)

        # def __str__(self):


def add_products_view(request):
    if request.method == 'POST':
        form = AddProductsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            Products.objects.create(
                tagline=data["tagline"],
                description=data['description'],
                product_image=data['product_image'],
                category=data['category'],
            )

            return HttpResponseRedirect('/')
            
    form = AddProductsForm()
    return render(request, 'genericform.html', {'form': form})

def product_detail_view(request,id):
    product = Products.objects.get(id=id)
    return render (request, 'product_detail_view.html',{'product': product})


def product_page(request):
    product = Products.objects.all()
    return render (request, 'product_page.html',{'product': product})
def delete():
    pass