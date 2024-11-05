from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from .models import *



class SectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    
    
class NewsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'get_photo', 'time_create', 'time_update')
    prepopulated_fields = {"slug": ("title",)}

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_photo.short_description = 'Фото'
    
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_photo', 'email', 'project')

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_photo.short_description = 'Фото'


class DocumentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'name_pdffile', 'is_published')
    list_display_links = ('id', 'title', 'is_published',)
    search_fields = ('title',)
    filter_horizontal = ('section',)
    list_filter = ('is_published', 'time_create', 'section')
    prepopulated_fields = {"slug": ("title",)}


class ImportResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'import_data',)


admin.site.register(ImportResult, ImportResultAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Documents, DocumentsAdmin)

admin.site.site_title = 'Администрирование сайта'
admin.site.site_header = 'Администрирование сайта'
