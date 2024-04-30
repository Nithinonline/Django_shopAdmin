from django.urls import path
from .views import register_user, user_login,user_logout,sso_user_login

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/',user_logout,name='logout'),
    path('login/sso/',sso_user_login,name='ssoLogin')
]