from django.contrib import admin

from .models import Buyer, Flowers

# Register your models here.


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name', )
    list_filter = ('balance', 'age', )
    fields = [('name', 'balance', 'age')]


@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited')
    search_fields = ('title', )
    list_filter = ('cost', 'size', 'age_limited', )
    fieldsets = (
        ('Flowers Info', {
            'fields': (('title', 'cost'), )
        }),
        ('Flowers Description', {
            'fields': ('description', ('size', 'age_limited'),)
        }),
    )