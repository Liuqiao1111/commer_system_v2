from django.contrib import admin
from django.utils.html import format_html
from .models import UserInfoModel, ItemModel, CategoryModel, OrderModel, CarModel, HotModel, CommentModel, ItemImageModel


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'address', 'money', 'phone', 'create_time')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'number', 'size', 'image_tag', 'category')

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="http://127.0.0.1:8000/image/{}" style="width:120px;height:70px;"/>'.format(obj.image))
        return ""

    image_tag.allow_tags = True
    image_tag.short_description = '照片'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'price', 'create_time', 'status')
    list_filter = ('status', 'create_time')  
    search_fields = ('user__username', 'item__name', 'price')  
    search_help_text = "搜索用户名、商品名称或价格"  
    list_per_page = 20  

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        
        # 处理状态的中文搜索
        status_dict = dict(OrderModel.STATUS_CHOICES)
        status_reverse = {v: k for k, v in status_dict.items()}
        
        if search_term in status_reverse:
            queryset |= self.model.objects.filter(status=status_reverse[search_term])
            
        return queryset, use_distinct


class CarAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'price', 'is_pay', 'create_time')


class HotAdmin(admin.ModelAdmin):
    list_display = ('name', 'item')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'create_time')


class ItemImageAdmin(admin.ModelAdmin):
    list_display = ('item', 'image_tag', 'description', 'create_time')
    search_fields = ('item__name', 'description')
    list_filter = ('create_time',)

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="http://127.0.0.1:8000/image/{}" style="width:120px;height:70px;"/>'.format(obj.image))
        return ""

    image_tag.allow_tags = True
    image_tag.short_description = '附加图片'


admin.site.register(UserInfoModel, UserInfoAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ItemModel, ItemAdmin)
admin.site.register(OrderModel, OrderAdmin)
admin.site.register(CarModel, CarAdmin)
admin.site.register(HotModel, HotAdmin)
admin.site.register(CommentModel, CommentAdmin)
admin.site.register(ItemImageModel, ItemImageAdmin)
admin.site.site_header = '电商后台管理系统'
