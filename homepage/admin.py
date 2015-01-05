from django.contrib import admin

from homepage.models import Pages, Items
# Register your models here.

class PagesAdmin(admin.ModelAdmin):
    list_display = ['header','desc','type']

class ItemsAdmin(admin.ModelAdmin):
    list_display = ['header','text','page', 'image']
    

admin.site.register(Pages, PagesAdmin)
admin.site.register(Items, ItemsAdmin)