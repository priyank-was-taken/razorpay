from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Razor)
class RazorAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]