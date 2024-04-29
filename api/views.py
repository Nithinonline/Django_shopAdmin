# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello Admin")


from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Shop
from .serializers import ShopSerializer
from rest_framework import status,serializers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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

#Adding new shop
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_shop_details(request):
    shop=ShopSerializer(data=request.data)

    #validating for already existing data
    if Shop.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    if shop.is_valid():
        shop.save()
        return Response(shop.data)
    else:
        print(shop.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST,)
    



#view shop
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_shop(request):

    paginator=PageNumberPagination()
    paginator.page_size=5

    # if request.query_params:
    #     shop=Shop.objects.filter(**request.query_params.dict())

    # else:
    shop=Shop.objects.all()

    # if shop:
    #     serializer=ShopSerializer(shop,many=True)
    #     return Response(serializer.data)
    result_page=paginator.paginate_queryset(shop,request)
    serializer=ShopSerializer(result_page,many=True)

    # else:
    return paginator.get_paginated_response(serializer.data)


#update shop details
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_shop_details(request,pk):
    try:
       shop=Shop.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,data="Error finding shop")

    data=ShopSerializer(instance=shop,data=request.data,partial=True)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)
    

#Delete shop
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_shop(request, pk):
    try:
        shop = Shop.objects.get(pk=pk)
        shop.delete()
        return Response(data={"message": "Deleted successfully"})
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
	





