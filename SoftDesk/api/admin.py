#
#
# from django.contrib import admin
# from shop.models import Category, Product, Article
#
#
# class CategoryAdmin(admin.ModelAdmin):
#
#     list_display = ('name', 'active')
#
#
# class ProductAdmin(admin.ModelAdmin):
#
#     list_display = ('name', 'category', 'active')
#
#
# class ArticleAdmin(admin.ModelAdmin):
#
#     list_display = ('name', 'product', 'category', 'active')
#
#     @admin.display(description='Category')
#     def category(self, obj):
#         return obj.product.category
#
#
from django.contrib import admin

from api.models import Contributor
from api.models import Project
from api.models import Issue
from api.models import Comment

# Register your models here.

admin.site.register(Contributor)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
