from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'id']


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'author', 'time_create', 'id']


@admin.register(models.Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'time_create', 'time_update', 'id']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website']



