from django.contrib import admin
from .models import Category, Article, SocialMedia, MiscLinks

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('title', 'created_at', 'public')
    search_fields = ('title', 'content', 'categories')
    ordering = ('-created_at',)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')


class SocialMediaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'public')
    search_fields = ('name', 'public')
    ordering = ('name',)

class MiscLinksAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'public')
    search_fields = ('name', 'public')
    ordering = ('-created_at',)


# REGISTRAMOS LOS MODELOS EN LA ADMINISTRACIÓN DEL SITIO
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(MiscLinks, MiscLinksAdmin)