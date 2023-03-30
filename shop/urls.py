"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from . import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

import debug_toolbar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include(debug_toolbar.urls))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                    document_root=settings.MEDIA_ROOT)
    
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collection', views.CollectionViewSet)
router.register('cart', views.CartViewSet, basename='cart')
router.register('customers', views.CustomerViewSet, basename='customer')
router.register('orders', views.OrderViewSet, basename="orders")


products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
products_router.register('images', views.ProductImageViewSet, basename='product-images')

cart_router = routers.NestedDefaultRouter(router, 'cart', lookup='cart')
cart_router.register('items', views.CartItemViewSet, basename='cart-items-detail')  
urlpatterns = router.urls + products_router.urls + cart_router.urls
