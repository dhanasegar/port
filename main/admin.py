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

class UserProfileAdminForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def clean_cv(self):
        cv = self.cleaned_data.get('cv')
        if cv:
            # Convert the file to binary data
            self.instance.cv_binary = cv.read()  # Store the binary content
       # Close the file after reading it
        return cv
    

class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileAdminForm
    list_display = ('id', 'user')
    fields = ('user', 'title', 'bio', 'skills', 'cv')  # Include the FileField for admin upload

# Registering UserProfileAdmin to the admin site
admin.site.register(UserProfile, UserProfileAdmin)


@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name',)
    search_fields = ('name', 'email',)
    list_filter = ('timestamp',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')


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
