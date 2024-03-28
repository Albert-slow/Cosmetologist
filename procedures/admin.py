from django.contrib import admin
from .models import CategoryModel, ProcedureModel, CartModel, PostModel, CommentsModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(ProcedureModel)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ['procedure_title', 'procedure_category', 'procedure_created_at']
    search_fields = ['procedure_title']
    list_filter = ['procedure_created_at']


@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_add_date']


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_author', 'post_date']
    search_fields = ['post_title']
    list_filter = ['post_date']


@admin.register(CommentsModel)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']
    search_fields = ['name']
    list_filter = ['post']


