from django.contrib import admin
from .models import MyUser, FollowMyUser, Post, CommentPost, LikePost


# Register your models here.

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_display_links = ('id', 'user')


# admin.site.register(MyUser)
admin.site.register(FollowMyUser)
admin.site.register(Post)
admin.site.register(CommentPost)
admin.site.register(LikePost)
