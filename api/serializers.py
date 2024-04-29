from django.db.models import fields
from rest_framework import serializers
from .models import Shop


class ShopSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Shop
        fields=('name','address','city','phone','image','id')