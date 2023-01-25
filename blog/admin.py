from django.contrib import admin
from django.contrib.admin import register
from .models import Post, Category

@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]

@register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ( "title", "author", "slug", "content", "image", "status", "excerpt", "category")
    list_display = ['title']
    
