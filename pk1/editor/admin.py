from django.contrib import admin

# Register your models here.
from editor.models import editor_news

class editor(admin.ModelAdmin):
    list_display = ('news_title','news_desc')
admin.site.register(editor_news,editor)