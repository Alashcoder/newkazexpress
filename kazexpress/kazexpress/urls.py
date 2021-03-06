"""kazexpress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mainpage.views import *
from django.urls import reverse
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    path('about_us',about_us,name='about'),
    path('store', store, name='store'),
    path('search',search,name='search'),
    path('cart', include('cart.urls', namespace='cart')),
    # path('product/<int:id>',product_page,name='product_page'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
 #   path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('product/<int:pk>',ProductDetailView.as_view(),name='product-detail')
   # path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
