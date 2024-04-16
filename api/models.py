from django.db import models


class Shop(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    city=models.CharField(max_length=30)
    phone=models.CharField(max_length=14,default='N/A')
    image=models.ImageField(default='default.jpg',upload_to='media/')



    def __str__(self) -> str:
        return self.name