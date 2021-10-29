from django.db.models.fields import IntegerField
from django.shortcuts import render
from website_app.models import Products
from django.shortcuts import render,  HttpResponseRedirect, redirect
from django import forms
from website_app import views


# Create your views here.
def index_view(request):
    product = Products.objects.all()

    return render(request,'index.html',{'product':product})

class AddProductsForm(forms.ModelForm):
    class Meta:
        model= Products
        fields= ('tagline','description')
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
            )

            return HttpResponseRedirect('/')
            
    form = AddProductsForm()
    return render(request, 'genericform.html', {'form': form})

def product_detail_view(request,id):
    product = Products.objects.get(id=id)
    return render (request, 'product_detail_view.html',{'product': product})
