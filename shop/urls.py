from django.urls import path
from shop.views import checkout, detail, index

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', detail, name='detail'),
    path('checkout/', checkout, name='checkout'),
]
