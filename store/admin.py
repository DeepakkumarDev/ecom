from django.contrib import admin,messages
from django.db.models import Count
from django.urls import reverse 
from django.utils.html import format_html,urlencode
from . import models


    

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # fields=['title','slug']
    exclude=['promotions']
    actions=['clear_inventory']
    list_display=['title','unit_price','inventory_status','collection_title']
    list_editable=['unit_price']
    list_filter=['collection','last_update',InventoryFilter]
    list_per_page=10
    list_select_related=['collection']


    def collection_title(self,product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory<10:
            return 'Low'
        return 'ok'
    
    @admin.action(description='Clear inventory')
    def clear_inventory(self,request,queryset):
        updated_count=queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} Product were succesfully updated ',
             messages.ERROR

        #    messages.SUCCESS
        )
    



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','membership']
    list_editable=['membership']
    list_per_page=10
    ordering=['first_name','last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','placed_at','customer']

    


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display=['title','product_count']


    @admin.display(ordering='products_count')
    def product_count(self,collection):
        # reverse('admin:app_model_page')
        url=(
            reverse('admin:store_product_changelist')
            +'?'
            + urlencode({
                'collection__id':str(collection.id)
            }))
        return format_html('<a href="{}">{}</a>',url,collection.products_count)
        # return format_html('<a href="http://google.com">{}</a>',collection.products_count)
        # return collection.products_count
    
    def get_queryset(self,request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
