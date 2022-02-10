from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'id']



@admin.register(models.Post)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ['author', 'name', 'category', 'time_create', 'time_update', 'id']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website']



