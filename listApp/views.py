from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Product

# Create your views here.
def home(request):
    return render(request, 'list/home.html')

class productListView(ListView):
    template_name = "list/list.html"
    model = Product
    context_object_name = "products"