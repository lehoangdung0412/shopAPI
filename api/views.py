from .serializers import *
from . import models
from rest_framework import viewsets, permissions, generics
from .permissions import IsOwner
from django.shortcuts import Http404


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customers.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if (self.action == 'list') | (self.action == 'retrieve'):
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class DeliveryAddViewSet(viewsets.ModelViewSet):
    queryset = models.DeliveryAdds.objects.all()
    serializer_class = DeliveryAddSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Orders.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if (self.action == 'list') | (self.action == 'retrieve'):
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItems.objects.all()
    serializer_class = OrderItemSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = models.Login.objects.all()
    serializer_class = LoginSerializer


class CurrentUserViewSet(viewsets.GenericViewSet, generics.RetrieveUpdateAPIView):
    queryset = models.Customers.objects
    serializer_class = CustomerSerializer
    permission_classes = (IsOwner,)

    def get_view_name(self):
        name = "Current User"
        return name

    def get_queryset(self):
        # remove 'current-user/pk' url and its actions
        if self.action in ('retrieve', 'update', 'partial_update'):
            raise Http404
        # get Customer object who is logging in
        try:
            return self.queryset.filter(owner=self.request.user).get()
        except Exception:  # fix 'Anonymous User' error when log out and log in by admin
            raise Http404

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        return queryset


class OrdersByCurrentUserViewSet(viewsets.GenericViewSet, generics.ListAPIView):
    queryset = models.Orders.objects
    serializer_class = OrderSerializer
    permission_classes = (IsOwner, )

    def get_view_name(self):
        name = "Current User Order"
        return name

    def get_queryset(self):
        try:
            return self.queryset.filter(customer=self.request.user.owner)
        except AttributeError:
            raise Http404
