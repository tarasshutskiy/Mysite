from django.contrib import admin
from . import models
from modeltranslation.admin import TranslationAdmin

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
    save_on_top = True


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'comment', 'author']
    search_fields = ('post',)
    save_on_top = True


class CommentInline(admin.TabularInline):
    model = models.Comment


@admin.register(models.Post)
class PostAdmin(TranslationAdmin):
    list_display = ['id', 'author', 'name', 'category', 'time_create', 'time_update', 'is_published', ]
    list_display_links = ('author', 'name')
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    search_fields = ('name', 'descriptions')
    inlines = [
        CommentInline,
    ]
    save_on_top = True
    save_as = True

