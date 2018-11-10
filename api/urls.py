from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_jwt.views import obtain_jwt_token


router = routers.SimpleRouter(trailing_slash=False)
router.register('customers/', views.CustomerViewSet)
router.register('products/', views.ProductViewSet)
# router.register('delivery', views.DeliveryAddViewSet)
router.register('orders/', views.OrderViewSet)
router.register('order-items/', views.OrderItemViewSet)
router.register('categories/', views.CategoryViewSet)
# router.register('login', views.LoginViewSet)
router.register('current-user/orders/', views.OrdersByCurrentUserViewSet)
router.register('current-user/', views.CurrentUserViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/sessions/', obtain_jwt_token, name='create-token'),
]
