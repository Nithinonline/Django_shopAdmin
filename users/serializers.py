from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','email','password','phone','id','image']
        extra_kwargs={'password':{'write_only':True}}


    def create(self,validated_data):
        user = CustomUser.objects.create(**validated_data) 
        user.set_password(validated_data['password'])
        user.save()
        return user
  

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return value