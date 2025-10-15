from django.contrib import admin
from .models import Client, Order

#admin.site.register(Client)
#admin.site.register(Order)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company', 'created_at')
    search_fields = ('name', 'company')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'amount', 'status', 'created_by', 'created_at')
    list_filter = ('status', 'client')
    search_fields = ('title',)


