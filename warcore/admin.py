from django.contrib import admin
from .models import Arms, News, UserProfile, World
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass

class ArmsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'desc',
        'sx',
        'infantry_attack',
        'tank_attack',
        'air_attack',
        'sea_attack',
        'build_attack',
        'build_limit',
        'defense',
        'kj',
        'price',
        'time',
        'img_id'
    )

    readonly_fields = ('img_id',)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'type',
        'content',
        'status',
        'crate_at'
    )

class WorldAdmin(admin.ModelAdmin):
    list_display = (
        'world_name',
        'init_gold'
    )

class BaseAdmin(admin.ModelAdmin):
    list_display = (

    )

admin.site.register(Arms, ArmsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(World, WorldAdmin)