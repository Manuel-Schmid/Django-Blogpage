from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from blog.models import User, Category, Post

admin.site.register(User, UserAdmin)
admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width=150 height=150/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ('title', 'date_created', 'category', 'owner', 'image_tag')


admin.site.register(Post, PostAdmin)

fields = ( 'image_tag', )
readonly_fields = ('image_tag',)