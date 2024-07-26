from django.contrib import admin

from .models import Menulink

@admin.register(Menulink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ["id","text", "url_or_path",]
    list_display_links = ["id","text", "url_or_path",]
    search_fields = ["id","text", "url_or_path",]
    
    