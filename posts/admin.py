from django.contrib import admin
from .models import Post, Like, Dislike

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass

@admin.register(Dislike)
class DislikeAdmin(admin.ModelAdmin):
    pass
