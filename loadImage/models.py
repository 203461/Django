from django.db import models

# Create your models here.
class imageModel(models.Model):
    name_img = models.CharField(max_length=75, null=True)
    url_img = models.ImageField(blank='', default="", upload_to='img/')
    format_img = models.CharField(max_length=75, null=True)
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)