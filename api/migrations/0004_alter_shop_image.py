# Generated by Django 5.0.4 on 2024-04-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_shop_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='../../assets/'),
        ),
    ]