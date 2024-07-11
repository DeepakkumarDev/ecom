from django.shortcuts import render
from django.shortcuts import get_object_or_404 
from django.http import HttpResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from django.db.models import Count
from .models import Product,Collection
from .serializers import ProductSerializer,CollectionSerializer
# Create your views here.

class ProductList(APIView):
    def get(self,request):
        queryset=Product.objects.select_related('collection').all()
        serializer=ProductSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data)
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class ProductDetail(APIView):
    def get(self,request,id):
        product=get_object_or_404(Product,pk=id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    def put(self,request,pk):
        product=get_object_or_404(Product,pk=id)
        serializer=ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def delete(self,request,pk):
        product=get_object_or_404(Product,pk=id)
        if product.orderitems.count()>0:
            return Response({'error':'product can not be deleted because it is associated with an order item.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET','POST'])
def product_list(request):
    if request.method=='GET':
        queryset=Product.objects.select_related('collection').all()
        serializer=ProductSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print(serializer.validated_data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        # if serializer.is_valid():
        #     serializer.validated_data
        #     return Response('ok')
        # else:
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE'])
def product_detail(request,id):
    product=get_object_or_404(Product,pk=id)
    if request.method=='GET':
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method=='DELETE':
        # if product.orderitem_set.count()>0:
        if product.orderitems.count()>0:
            return Response({'error':'product can not be deleted because it is associated with an order item.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view(['GET','POST'])
def collection_list(request):
    if request.method=='GET':
        queryset=Collection.objects.annotate(products_count=Count('product')).all()
        serializer=CollectionSerializer(queryset,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class CollectionList(APIView):
    def get(self,request):
        queryset=Collection.objects.annotate(products_count=Count('product')).all()
        serializer=CollectionSerializer(queryset,many=True)
        return Response(serializer.data)  
    def post(self,request):
        serializer=CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)            


def CollectionDetail(APIView):
    def get(self,request,pk):
        queryset = Collection.objects.annotate(products_count=Count('product'))
        collection = get_object_or_404(queryset, pk=pk)        
        serializer=CollectionSerializer(collection)
        return Response(serializer.data)
    
    def put(self,request,pk):
        queryset = Collection.objects.annotate(products_count=Count('product'))
        collection = get_object_or_404(queryset, pk=pk)          
        serializer=CollectionSerializer(collection)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def delete(self,request,pk):
        queryset = Collection.objects.annotate(products_count=Count('product'))
        collection = get_object_or_404(queryset, pk=pk)
        if collection.products.count()>0:
            return Response({'error':'Collection can not be deleted it include one or more products. '},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE']) 
def collection_detail(request,pk):
    queryset = Collection.objects.annotate(products_count=Count('product'))
    # Then, filter by pk and get the object
    collection = get_object_or_404(queryset, pk=pk)    
    if request.method=='GET':
        serializer=CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=CollectionSerializer(collection)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method=='DELETE':
        if collection.products.count()>0:
            return Response({'error':'Collection can not be deleted it include one or more products. '},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
