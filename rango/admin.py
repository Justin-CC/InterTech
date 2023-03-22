from django.contrib import admin
from rango.models import Dish, User, Comment, Receive


class UserAdmin(admin.ModelAdmin):
    list_display = ('userid','username', 'phone', 'email')

class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('dishname',)}
    list_display = ('dishid', 'dishname', 'type', 'price')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentid','dish', 'user')


class ReceiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')

admin.site.register(Dish, DishAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Receive, ReceiveAdmin)


