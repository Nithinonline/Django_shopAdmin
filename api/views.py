


from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Shop,ShopImages
from .serializers import ShopSerializer,ShopImageSerializer
from rest_framework import status,serializers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def ApiOverview(request):
#     api_urls = {
#         'all_items': '/',
#         'Search by name': '/?name=shop_name',
#         'Search by city': '/?city=city_name',
#         'Add': '/create',
#         'Update': '/update/pk',
#         'Delete': '/item/pk/delete'
#     }
 
#     return Response(api_urls)

# #Adding new shop
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_shop_details(request):
#     shop=ShopSerializer(data=request.data)
#     print(shop)

#     #validating for already existing data
#     if Shop.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')
    
#     if shop.is_valid():
#         shop.save()
#         return Response(shop.data)
#     else:
#         print(shop.errors)
#         return Response(status=status.HTTP_400_BAD_REQUEST,)
    



# #view shop
# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def view_shop(request):

#     paginator=PageNumberPagination()
#     paginator.page_size=5

#     # if request.query_params:
#     #     shop=Shop.objects.filter(**request.query_params.dict())

#     # else:
#     shop=Shop.objects.all()

#     # if shop:
#     #     serializer=ShopSerializer(shop,many=True)
#     #     return Response(serializer.data)
#     result_page=paginator.paginate_queryset(shop,request)
#     serializer=ShopSerializer(result_page,many=True)

#     # else:
#     return paginator.get_paginated_response(serializer.data)


# #update shop details
# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def update_shop_details(request,pk):
#     try:
#        shop=Shop.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND,data="Error finding shop")
#     if shop.user==str(request.user):
#        data=ShopSerializer(instance=shop,data=request.data,partial=True)
#        if data.is_valid():
#           data.save()
#           return Response(data.data)
#        else:
#           return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)
       
#     else:
#         return Response({"error":"you are not allowd to update"},status=status.HTTP_403_FORBIDDEN)   
    

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
	
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_shop_image(request, pk):
    try:
        shop_image = ShopImages.objects.get(pk=pk)
        shop_image.delete()
        return Response(data={"message": "Image Deleted successfully"})
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)     
# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def delete_image(request,pk):
    
#        shop=Shop.objects.get(pk=pk)
#        print(request.data,shop)
   

 

##########################################################################################################################

#Class Based View


class CustomPagination(PageNumberPagination):
    # page_size = 5
    # page_size_query_param = 'page'
    max_page_size = 100

class shopViewSet(viewsets.ModelViewSet):
    queryset=Shop.objects.all()
    serializer_class=ShopSerializer
    permission_classes=[IsAuthenticated]
    pagination_class=CustomPagination

   


    # def partial_update(self, request, *args, **kwargs):
    #     print(request.data)
    #     id = self.kwargs.get('pk')
    #     try:
    #         shop = Shop.objects.get(pk=id)
    #     except Shop.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND, data="Error finding shop")

    #     shop_serializer = ShopSerializer(instance=shop, data=request.data, partial=True)
    #     if not shop_serializer.is_valid():
    #         return Response(shop_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     shop_instance = shop_serializer.save()

    #     uploaded_images = request.FILES.getlist('images')

    #     # If no images are uploaded, skip deletion process
    #     if uploaded_images:
    #         uploaded_image_names = [image.name for image in uploaded_images]

    #         existing_images = ShopImages.objects.filter(shop=shop_instance)
            
    #         for image in existing_images:
    #             if image.image.name not in uploaded_image_names:
    #                 image.delete()

    #     for image in uploaded_images:
    #         shop_image_serializer = ShopImageSerializer(data={'image': image, 'shop': [shop_instance.pk]}, partial=True)
    #         if shop_image_serializer.is_valid():
    #             shop_image_serializer.save()
    #         else:
    #             return Response(shop_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     return Response(shop_serializer.data)

    



    
    
            
    


