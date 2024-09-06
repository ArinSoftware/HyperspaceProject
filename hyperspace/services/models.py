from django.db import models
from django.utils.text import slugify  # Import the slugify utility to create slugs from strings

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        super(Service, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']  # Default ordering by title in ascending order
        verbose_name = 'Service'  # Human-readable name for the model in singular form
        verbose_name_plural = 'Services'  # Human-readable name for the model in plural form

