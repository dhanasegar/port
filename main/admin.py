from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Testimonial,
    Media,
    Portfolio,
    Blog,
    Certificate,
    Skill
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name',)
    search_fields = ('name', 'email',)
    list_filter = ('timestamp',)
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    fields = ('thumbnail', 'thumbnail_url', 'name', 'role', 'quote', 'is_active')
    readonly_fields = ('thumbnail_url',)  # Make thumbnail_url read-only

    def thumbnail_url(self, obj):
        # This will display the thumbnail URL in the admin interface
        if obj.thumbnail:
            return obj.thumbnail.url
        return None


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')