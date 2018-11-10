from .serializers import *
from . import models
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customers.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = ProductSerializer


class DeliveryAddViewSet(viewsets.ModelViewSet):
    queryset = models.DeliveryAdds.objects.all()
    serializer_class = DeliveryAddSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Orders.objects.all()
    serializer_class = OrderSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = CategorySerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItems.objects.all()
    serializer_class = OrderItemSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = models.Login.objects.all()
    serializer_class = LoginSerializer
