from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, DeleteView, View
from django.views.generic.edit import CreateView, UpdateView
from .models import Category, Product
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request, 'list/home.html')

class homeView(ListView):
    template_name = 'list/home.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        favourites = self.request.session.get("favourites", [])
        return Product.objects.filter(slug__in=favourites) if favourites else []

class productListView(ListView):
    template_name = "list/list.html"
    model = Product
    context_object_name = "products"

class product_detail(DetailView):
    template_name = "list/productDetails.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        request = self.request
        listaFavourites = request.session.get("favourites",[])

        if product.slug not in listaFavourites:
            context["is_favourite"] = False
        else:
            context["is_favourite"] = True
        return context

class AddFavoriteView(View):
    def post(self, request):
        product_slug = request.POST["product_slug"]
        listaFavourites = request.session.get("favourites",[])
        listaFavourites.append(product_slug)
        request.session["favourites"] = listaFavourites
        return HttpResponseRedirect(product_slug)

class product_add(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'list/productAdd.html'
    success_url = '/'

class product_update(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'list/productUpdate.html'
    success_url = '/'

class product_delete(DeleteView):
    model = Product
    fields = '__all__'
    template_name = 'list/productDelete.html'
    success_url = '/'