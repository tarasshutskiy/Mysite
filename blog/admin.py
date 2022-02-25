from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    prepopulated_fields = {"slug": ("name",)}



@admin.register(models.Post)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ['author', 'name', 'category', 'time_create', 'time_update' ]
    prepopulated_fields = {"slug": ("name",)}




