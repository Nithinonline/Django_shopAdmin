from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import shopViewSet
from .views import delete_shop,delete_shop_image,send_email


router=DefaultRouter()
router.register(r'shops',shopViewSet)

# urlpatterns = [
#     path('',views.ApiOverview,name='home'),
#     path('create/',views.add_shop_details,name='add-shop'),
#     path('all/',views.view_shop,name='view-shops'),
#     path('update/<int:pk>/',views.update_shop_details,name='update-shop'),
#     path('delete/<int:pk>/',views.delete_shop,name='delete-shop')
# ]


urlpatterns = [
    path('',include(router.urls)),
    path('delete/<int:pk>',delete_shop,name='delete-shop'),
    path('deleteImage/<int:pk>',delete_shop_image,name='delete-shop-image'),
    path('mail',send_email,name='email')

]
