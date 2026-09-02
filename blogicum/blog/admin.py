from django.contrib import admin
from .models import Location, Category, Post


admin.site.empty_value_display = 'Не задано'


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )

    list_display = (
        'name',
    )

    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )

    list_display = (
        'title',
        'slug',
        'short_description'
    )

    list_editable = (
        'slug',
    )

    search_fields = ('title',)

    @admin.display(description='Описание')
    def short_description(self, obj):
        if obj.description:
            if len(obj.description) > 50:
                return obj.description[:50] + '...'
            else:
                return obj.description


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'location',
        'category',
    )

    list_editable = (
        'pub_date',
        'author',
        'location',
        'category',
    )

    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
