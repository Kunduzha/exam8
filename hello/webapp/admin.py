from django.contrib import admin

# Register your models here.
from webapp.models import Goods, Category, Review


class GoodAdmin(admin.ModelAdmin):
    good_display = ['id', 'name', 'image', 'category']
    list_filter = ['category', 'name']
    search_fields = ['name']
    fields = ['name', 'category', 'description', 'image']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']


class ReviewAdmin(admin.ModelAdmin):
    fields = ['good', 'user', 'text_review', 'rating', 'moderation']
    review_display = ['id', 'user', 'text_review', 'rating', 'moderation']


admin.site.register(Goods, GoodAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin,)