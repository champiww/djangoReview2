"""
URL configuration for review2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeView.as_view(), name='home'),
    path('list', views.productListView.as_view(), name='list'),
    path('add', views.product_add.as_view(),name='product-add'),
    path('favourite', views.AddFavoriteView.as_view()),
    path('<slug:slug>', views.product_detail.as_view(),name='product-detail'),
    path('<slug:slug>/update', views.product_update.as_view(),name='product-update'),
    path('<slug:slug>/delete', views.product_delete.as_view(),name='product-delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)