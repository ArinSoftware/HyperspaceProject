from django.contrib import admin
from .models import Blog 

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  
    search_fields = ('title', 'content')  
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ['author']  