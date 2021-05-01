from django.contrib import admin

# Register your models here.
from webapp.models import Goods, Category


class GoodAdmin(admin.ModelAdmin):
    good_display = ['id', 'name', 'image', 'category']
    list_filter = ['category', 'name']
    search_fields = ['name']
    fields = ['name', 'category', 'description', 'image']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Goods, GoodAdmin)
admin.site.register(Category, CategoryAdmin)
