from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Category, Post

admin.site.register(User, UserAdmin)
admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'category', 'owner',) # The variables from models.py

admin.site.register(Post, PostAdmin)