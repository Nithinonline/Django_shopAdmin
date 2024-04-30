from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','email','password','phone','id']
        extra_kwargs={'password':{'write_only':True}}


    def create(self,validated_data):
        user=CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone']
        )    
        user.set_password(validated_data['password'])
        user.save()
        return user