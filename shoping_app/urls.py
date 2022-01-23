from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('productdetail/<str:pk>', views.detail, name='detail'),
    path('checkout', views.checkout, name='checkout'),
]
