from rest_framework import serializers
from .models import Product as ProductModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        models = ProductModel
        fields = "__all__"