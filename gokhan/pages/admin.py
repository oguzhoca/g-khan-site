from django.contrib import admin
from .models import Test, Category


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

