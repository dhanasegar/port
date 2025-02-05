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
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(max_length=500, blank=True, null=True) 
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(upload_to='resumes/', null=True, blank=True)
    cv_binary = models.BinaryField(null=True, blank=True)  

    def save(self, *args, **kwargs):
        if self.cv and not self.cv_binary:
            with self.cv.open('rb') as file:
                self.cv_binary = file.read()
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username if self.user else "Unlinked Profile"



class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = 'Employment'
        verbose_name = 'Testimonial'
        ordering = ["id"]

    thumbnail = models.URLField(blank=True, null=True) 
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Media(models.Model):
    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    image = models.URLField(blank=True, null=True) 
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Education'
        verbose_name = 'Portfolio'
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)  
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Blog(models.Model):
    class Meta:
        verbose_name_plural = 'Projects'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True) 
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Certificate(models.Model):
    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=255)
    file = models.BinaryField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


# class SocialMediaLink(models.Model):
#     class Meta:
#         verbose_name_plural = 'Social Media Links'
#         verbose_name = 'Social Media Link'

#     PLATFORM_CHOICES = [
#         ('facebook', 'Facebook'),
#         ('instagram', 'Instagram'),
#         ('twitter', 'Twitter'),
#         ('linkedin', 'LinkedIn'),
#     ]

    
#     platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, unique=True)
#     url = models.URLField(max_length=500, blank=True, null=True)


#     def __str__(self):
#         return f"{self.get_platform_display()} - {self.url}"
    
class SocialMediaLink(models.Model):
    name=models.TextField(default='-')
    fb=models.TextField(default='-')
    ig=models.TextField(default='-')
    tw=models.TextField(default='-') 
    li=models.TextField(default='-')

    def __str__(self):
        return "Social Media Links"