from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view()
def product_list(request):
    return Response("ok")

@api_view()
def product_detail(request, id):
    response = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(response)
    return Response(serializer.data)
