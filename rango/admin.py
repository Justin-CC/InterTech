from django.contrib import admin
from rango.models import Dish, User, Comment


#
# class PageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'url')
#

class UserAdmin(admin.ModelAdmin):
    list_display = ('userid','username', 'phone', 'email')

class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('dishname',)}
    list_display = ('dishid', 'dishname', 'type', 'price')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentid','dish', 'user')


admin.site.register(Dish, DishAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)

# admin.site.register(Page, PageAdmin)


# Register your models here.
