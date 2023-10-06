from django.db import models

# Create your models here.
class Image(models.Model):
    original_image = models.ImageField(upload_to='original_images/')
    greyscale_image = models.ImageField(upload_to='greyscale_images/', null=True, blank=True)
