from ckeditor.fields import CKEditorWidget
from django.contrib import admin

from news.models import NewsModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    content = CKEditorWidget()
