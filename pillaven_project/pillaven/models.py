from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify

# Create your models here.
class Review_message(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    message = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review_message'
        verbose_name_plural = 'Review_messages'

    def __str__(self):
        return self.message  
    

class Projects(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)    

    def save(self, *args, **kwargs):
        if not self.slug:
            # First, create the base slug
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            # Keep checking if slug already exists
            while Projects.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)  

    preview_image = models.ImageField(upload_to='projects_images/')  
    website_image = models.ImageField(upload_to='projects_images/')  
    tagline = models.CharField(max_length=500)
    description = models.TextField()
    website_url = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=500, blank=True, null=True)
    linkedin_url = models.CharField(max_length=500, blank=True, null=True)
    instagram_url = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def site_image(self):
        return mark_safe(f"<img src='{self.preview_image.url}' height='45' style='border-radius: 50%;' >")
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name    