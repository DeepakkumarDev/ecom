from django.shortcuts import render
from django.http import HttpResponse 
from django.db.models import Q,F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.

def say_hello(request):
    query_set=Product.objects.values_list('id','title','collection__title')
    return render(request,'hello.html',{'name':"Deepak",'products':list(query_set)})











#  query_set=Product.objects.values('id','title','collection__title
# query_set=Product.objects.values('id','title')
# query_set=Product.objects.all()[5:5]
# query_set=Product.objects.all()[:5]
#  query_set=Product.objects.filter(collection__id=1).order_by('unit_price')
# query_set=Product.objects.order_by('unit_price','-title').reverse()
# uery_set=Product.objects.order_by('unit_price','-title')
# query_set=Product.objects.order_by('-title')
# query_set=Product.objects.order_by('title')
    # query_set=Product.objects.all()
    # list(query_set)
    # for product in list(query_set):
    #     print(product)
    # query_set=Product.objects.filter(inventory=F('unit_price'))
    # query_set=Product.objects.filter(title__icontains="coffee")
    # query_set=Product.objects.filter(last_update__year=2021)
    # query_set=Product.objects.filter(description__isnull=False)
    # query_set=Product.objects.filter(inventory__lt=10,unit_price__lt=20)
    # query_set=Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # query_set=Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))