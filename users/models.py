from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    image=models.ImageField(default='default-profile.jpg',upload_to='media/')



    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
 
        img=Image.open(self.image.path)
 
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)    