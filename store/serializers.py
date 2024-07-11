from rest_framework import serializers
from .models import Product,Collection
from decimal import Decimal

class CollectionSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=255)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','title','description','slug','inventory','unit_price','collection']
        # fields='__all__'
    # id=serializers.IntegerField()
    # title=serializers.CharField(max_length=255)
    # price=serializers.DecimalField(max_digits=6,decimal_places=2,source='unit_price')
    # price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    # collection=serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all()
    # )
    # # collection1=serializers.StringRelatedField(source='collection')
    # # collection=CollectionSerializer()
    # collection=serializers.HyperlinkedRelatedField(
    # queryset=Collection.objects.all(),
    # view_name='collection-detail'
    # )

    # def calculate_tax(self,product:Product):
    #     return product.unit_price*Decimal(1.1)
    
    # def validate(self,data):
    #     if data['password']!=data['confirm_password']:
    #         return serializers.ValidationError("Password do not match")
    #     return data
    

    
    


