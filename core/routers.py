from rest_framework.routers import DefaultRouter, SimpleRouter
from customer.views import CustomerViewSet
from product.views import ProductViewSet
from authentication.views import UserViewSet

router = DefaultRouter()
simrouter = SimpleRouter()

router.register('customers', CustomerViewSet)
router.register('products', ProductViewSet)
router.register('users', UserViewSet)