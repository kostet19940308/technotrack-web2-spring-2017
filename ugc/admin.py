from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from ugc.models import Post, Like


class LikeInline(GenericStackedInline):
    ct_field = 'target_type'
    ct_fk_field = 'target_id'
    model = Like
    max_num = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'short_text', 'updated_at')
    inlines = [
        LikeInline
    ]

    def short_text(self, post):
        return post.text[:100]


admin.site.register(Post, PostAdmin)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('author', 'target_object', 'updated_at')