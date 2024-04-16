from django.urls import path
from . import views

urlpatterns = [
    path('',views.ApiOverview,name='home'),
    path('create/',views.add_shop_details,name='add-shop'),
    path('all/',views.view_shop,name='view-shops'),
    path('update/<int:pk>/',views.update_shop_details,name='update-shop'),
    path('shop/<int:pk>/delete',views.delete_shop,name='delete-shop')
]
