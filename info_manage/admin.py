from django.contrib import admin
from django.utils.html import format_html
from .models import UserInfoModel, ItemModel, CategoryModel, OrderModel, CarModel, HotModel, CommentModel


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'address', 'money', 'phone', 'create_time')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'number', 'image_tag', 'category')

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="http://127.0.0.1:8000/image/{}" style="width:120px;height:70px;"/>'.format(obj.image))
        return ""

    image_tag.allow_tags = True
    image_tag.short_description = '照片'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'price', 'create_time')


class CarAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'price', 'is_pay', 'create_time')


class HotAdmin(admin.ModelAdmin):
    list_display = ('name', 'item')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'create_time')


admin.site.register(UserInfoModel, UserInfoAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ItemModel, ItemAdmin)
admin.site.register(OrderModel, OrderAdmin)
admin.site.register(CarModel, CarAdmin)
admin.site.register(HotModel, HotAdmin)
admin.site.register(CommentModel, CommentAdmin)
admin.site.site_header = '电商后台管理系统'
