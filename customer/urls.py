from django.urls import path
from customer.views import customer_list

urlpatterns = [
    path('customers', customer_list)
]