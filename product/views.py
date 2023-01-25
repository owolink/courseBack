from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, FavouriteProductSerializer
from .models import Product, FavouriteProduct
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'title', 'description')

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='add-favourite')
    def add_favourite(self, request,pk=None):
        user = request.user
        product = self.queryset.get(pk=pk)
        try:
            product = FavouriteProduct.objects.get(user=user, product=product)
            product.delete()
            return Response({'message': 'Product was deleted from favorites'})
        except FavouriteProduct.DoesNotExist:
            FavouriteProduct.objects.create(user=user, product=product)
            return Response({'message': 'Product was added to favorites'})

    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='favourites')
    def get_favourites(self, request):
        user = request.user
        product = FavouriteProduct.objects.filter(user=user)
        data = FavouriteProductSerializer(instance=product, many=True).data
        return Response(data)

    @action(methods=['GET'], detail=False, url_path='kira_products')
    def get_kira_products(self, products):
        products = Product.objects.filter( Q(customer__exact=2))
        data = ProductSerializer(instance=products, many=True).data
        return Response(data)