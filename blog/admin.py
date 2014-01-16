from django.contrib import admin
from blog.models import Post, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]


# add by frank at 2014.1.16 begin #
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]
# add by frank at 2014.1.16 end #

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)   # add by frank at 2014.1.16
