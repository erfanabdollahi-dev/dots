from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',TokenObtainPairView.as_view(), name='login') ,  
    path('register/',views.Regiseter.as_view(), name='login') ,  
    path('users/',views.UserListAPIView.as_view(), name='user-list-create')  , 
    path('users/<str:username>',views.UserDetailAPIView.as_view(), name='user-detail') ,  
]
