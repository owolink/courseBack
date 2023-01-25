from rest_framework.viewsets import ModelViewSet
from .serializers import CustomerSerializer
from .models import Customer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer