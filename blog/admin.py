from django.contrib import admin
from .models import Article, Category

# Register your models here.
admin.site.site_header = ("وبلاگ جنگویی")


@admin.action(description="انتشار مقالات انخاب شده")
def make_published(modeladmin, request, queryset):
    queryset.update(status="p")


@admin.action(description="پیش نویس شدن مقالات انتخاب شده")
def make_draft(modeladmin, request, queryset):
    queryset.update(status="d")



class CategoryAdmin(admin.ModelAdmin):
	list_display = ('position', 'title','slug', 'parent', 'status')
	list_filter = (['status'])
	search_fields = ('title', 'slug')
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tags', 'slug', 'author', 'jpublish', 'status','category_to_str')
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-publish']
    actions = [make_published, make_draft]


admin.site.register(Article, ArticleAdmin)