# from django.contrib import admin
# from django import forms
# from .models import (
#     UserProfile,
#     ContactProfile,
#     Testimonial,
#     Media,
#     Portfolio,
#     Blog,
#     Certificate,
#     Skill
# )

# class UserProfileAdminForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'

#     def clean_cv(self):
#         cv = self.cleaned_data.get('cv')
#         if cv:
#             # Convert the file to binary data
#             self.instance.cv_binary = cv.read()  # Store the binary content
#        # Close the file after reading it
#         return cv
    

# class UserProfileAdmin(admin.ModelAdmin):
#     form = UserProfileAdminForm
#     list_display = ('id', 'user')
#     fields = ('user', 'title', 'bio', 'skills', 'cv')  # Include the FileField for admin upload

# # Registering UserProfileAdmin to the admin site
# admin.site.register(UserProfile, UserProfileAdmin)


# @admin.register(ContactProfile)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('id', 'timestamp', 'name',)
#     search_fields = ('name', 'email',)
#     list_filter = ('timestamp',)


# @admin.register(Testimonial)
# class TestimonialAdmin(admin.ModelAdmin):
#     list_display = ('id','name','is_active')


# @admin.register(Media)
# class MediaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')


# @admin.register(Portfolio)
# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ('id','name','is_active')
#     readonly_fields = ('slug',)


# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('id','name','is_active')
#     readonly_fields = ('slug',)


# @admin.register(Certificate)
# class CertificateAdmin(admin.ModelAdmin):
#     list_display = ('id','name')


# @admin.register(Skill)
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ('id','name','score')
from django.contrib import admin
from django import forms
from .models import (
    UserProfile,
    ContactProfile,
    Testimonial,
    Media,
    Portfolio,
    Blog,
    Certificate,
    Skill
)

from django.utils.html import format_html
from django.contrib import admin


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', ] 
    search_fields = ['user__username', 'title']

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;"/>', obj.avatar)
        return "No Avatar"
    avatar_preview.short_description = 'Avatar Preview'




class MediaAdmin(admin.ModelAdmin):
    list_display = ['name',  'is_image']
    search_fields = ['name', 'url']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image}" width="50" height="50"/>'
        return "No Image"
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'



class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name',  'is_active']
    search_fields = ['name', 'description']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image}" width="50" height="50"/>'
        return "No Image"
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name', 'description']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image}" width="50" height="50"/>'
        return "No Image"
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'



class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name', 'quote']

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return f'<img src="{obj.thumbnail}" width="50" height="50"/>'
        return "No Thumbnail"
    thumbnail_preview.allow_tags = True
    thumbnail_preview.short_description = 'Thumbnail Preview'


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')
    
@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name',)
    search_fields = ('name', 'email',)
    list_filter = ('timestamp',)    


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Testimonial, TestimonialAdmin)

