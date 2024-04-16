from django.db import models


class Shop(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    city=models.CharField(max_length=30)
    phone=models.IntegerField()



    def __str__(self) -> str:
        return self.name