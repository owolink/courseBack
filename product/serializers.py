from rest_framework import serializers
from .models import Product, FavouriteProduct
from authentication.serializers import UserSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError('Название и описание должны различаться!')
        return data

class FavouriteProductSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    product_data = ProductSerializer(source='product')

    class Meta:
        model = FavouriteProduct
        exclude = ['user', 'product']