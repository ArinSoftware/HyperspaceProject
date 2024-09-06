from django.contrib import admin
from .models import Service  # Import the Service model

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'slug')  # Display these fields in the list view
    search_fields = ('title', 'description')  # Add search functionality for these fields
    list_filter = ('is_featured',)  # Add filter options based on the 'is_featured' field
    prepopulated_fields = {"slug": ("title",)}  # Automatically populate the slug field from the title

# Alternatively, you can use this instead of the decorator:
# admin.site.register(Service, ServiceAdmin)

