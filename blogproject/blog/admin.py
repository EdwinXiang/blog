from django.contrib import admin
from .models import Category,Port,Tag

# Register your models here.
# 注册自己写的数据模型 告诉Django后台

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


admin.site.register(Category)
admin.site.register(Port,PostAdmin)
admin.site.register(Tag)
