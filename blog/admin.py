# coding=utf8
from django.contrib import admin
from blog.models import Post, Tag, Category
from blog.forms import PostAdminForm


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    """
    分类管理
    add by frank at 2014.2.7
    """
    fields = ('name', 'parent', )
    search_fields = ('name', )
    list_display = ('name', 'parent', )


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'author', 'create_time', 'modify_time', 'category', 'status']
    list_filter = ['modify_time', 'category', 'tags', 'status']
    prepopulated_fields = {'slug': ['title']}  # ':'后面最好添加空格,根据title预填充slug
    form = PostAdminForm

    # class Media:
    #     js = (
    #         '/static/js/tinymce/tinymce.min.js',
    #         '/static/js/tinymce/config.js',
    #         # '/static/js/ckeditor/ckeditor.js',
    #         # '/static/js/ckeditor/config.js',
    #     )


# add by frank at 2014.1.16 begin #
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
# add by frank at 2014.1.16 end #

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
