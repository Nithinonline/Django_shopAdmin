# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello Admin")


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Shop
from .serializers import ShopSerializer
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by name': '/?name=shop_name',
        'Search by city': '/?city=city_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)