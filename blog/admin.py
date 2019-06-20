from django.contrib import admin

# Register your models here.

from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name','cat_slug')
    prepopulated_fields = {'cat_slug': ('cat_name',)}
    fieldsets = [
        ('Name', {'fields': ['cat_name']}),
        (None, {'fields': ['cat_slug']}),
    ]

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','created_on','category')
    list_filter = ['created_on']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'slug']
    fieldsets = [
        ('Ana Bilgi', {'fields': ['title','slug']}),
        (None,{'fields': [('author','status','category')]}),
        ('İcerik', {'fields': ['content']}),
    ]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)