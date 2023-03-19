from django.contrib import admin
from rango.models import Dish, User, Comment


#
# class PageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'url')
# 
class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('dishname',)}


admin.site.register(Dish, DishAdmin)
admin.site.register(User)
admin.site.register(Comment)

# admin.site.register(Page, PageAdmin)


# Register your models here.
