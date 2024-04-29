from django.db import models
from PIL import Image
import os

# def custom_upload_path(instance, filename):
#     return '../../assets/{}'.format(filename)

class Shop(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    city=models.CharField(max_length=30)
    phone=models.CharField(max_length=10,default='N/A')
    image=models.ImageField(default='default.jpg',upload_to='media/')





    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
 
        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)    