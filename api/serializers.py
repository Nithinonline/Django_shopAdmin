from django.db.models import fields
from rest_framework import serializers
from .models import Shop
from .models import ShopImages  

class ShopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopImages  
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    images = serializers.SerializerMethodField()


    class Meta:
        model = Shop
        fields = ('name','address', 'city', 'phone','uploaded_images','images', 'id', 'user',)

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        shop = Shop.objects.create(**validated_data)

        shop_images_instances = [ShopImages(image=image) for image in uploaded_images]
        ShopImages.objects.bulk_create(shop_images_instances)

        shop.shopimages_set.set(shop_images_instances)
        return shop
    
    def get_images(self,obj):
        # images =  obj.shopimages_set.all()         Both line of codes are same.
        # print(obj)
        # serializer=ShopSerializer()
        # print(serializer.Meta.fields)
        print(obj)
        images = obj.shopimages_set.all() 
        return ShopImageSerializer(many=True, instance=images).data
        
