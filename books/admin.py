from django.contrib import admin
from . models import Category , Book
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title' , 'author' , 'price' , 'category' , 'status' , 'rental_price_day' , 'active']
