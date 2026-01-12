from django.urls import path
from Ecom_Shop import views

app_name = 'Ecom_Shop'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
    
]

