# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello Admin")


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Shop
from .serializers import ShopSerializer
from rest_framework import status,serializers
from django.core.exceptions import ObjectDoesNotExist

 
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

#Adding new shop
@api_view(['POST'])
def add_shop_details(request):
    shop=ShopSerializer(data=request.data)

    #validating for already existing data
    if Shop.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    if shop.is_valid():
        shop.save()
        return Response(shop.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    



#view shop
@api_view(['GET'])
def view_shop(request):

    if request.query_params:
        shop=Shop.objects.filter(**request.query_params.dict())

    else:
        shop=Shop.objects.all()

    if shop:
        serializer=ShopSerializer(shop,many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


#update shop details
@api_view(['PATCH'])
def update_shop_details(request,pk):
    try:
       shop=Shop.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data=ShopSerializer(instance=shop,data=request.data,partial=True)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)
    

#Delete shop
@api_view(['DELETE'])
def delete_shop(request, pk):
    try:
        shop = Shop.objects.get(pk=pk)
        shop.delete()
        return Response(data={"message": "Deleted successfully"})
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
	





