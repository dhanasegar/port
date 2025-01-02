from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=100, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(upload_to="skills", blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)  # Added URL field for images
    is_key_skill = models.BooleanField(default=False)

    def get_image(self):
        """
        Returns the image URL if available, else falls back to the uploaded file.
        """
        if self.image_url:
            return self.image_url
        if self.image:
            return self.image.url
        return "/static/default_skill.png"  # Default placeholder

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    avatar_url = models.URLField(blank=True, null=True)  # Added URL field for avatars
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def get_avatar(self):
        """
        Returns the avatar URL if available, else falls back to the uploaded file.
        """
        if self.avatar_url:
            return self.avatar_url
        if self.avatar:
            return self.avatar.url
        return "/static/default_avatar.png"  # Default placeholder

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]

    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    thumbnail_url = models.URLField(blank=True, null=True)  # Added URL field for thumbnails
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def get_thumbnail(self):
        """
        Returns the thumbnail URL if available, else falls back to the uploaded file.
        """
        if self.thumbnail_url:
            return self.thumbnail_url
        if self.thumbnail:
            return self.thumbnail.url
        return "/static/default_thumbnail.png"  # Default placeholder

    def __str__(self):
        return self.name


class Media(models.Model):
    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    image = models.ImageField(blank=True, null=True, upload_to="media")
    image_url = models.URLField(blank=True, null=True)  # Added URL field for images
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """
        Updates `is_image` based on whether the URL is provided.
        """
        if self.image_url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def get_image(self):
        """
        Returns the image URL if available, else falls back to the uploaded file.
        """
        if self.image_url:
            return self.image_url
        if self.image:
            return self.image.url
        return "/static/default_media.png"  # Default placeholder

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image_file = models.ImageField(upload_to="portfolio", blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def get_image(self):
        """
        Returns the image URL if available, else falls back to the uploaded file.
        """
        if self.image_url:
            return self.image_url
        if self.image_file:
            return self.image_file.url
        return "/static/default_portfolio.png"  # Default placeholder

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


# Repeat similar adjustments for Blog and Certificate models if needed.
