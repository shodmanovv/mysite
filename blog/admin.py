from django.contrib import admin
from .models import Post, Like, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] 
    list_filter = ['status', 'created', 'publish', 'author']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchstatusy = 'publish'
    ordering = ['status', 'publish']

admin.site.register([Like, Comment])