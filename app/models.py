from django.db import models
from django.utils.text import slugify

# Create your models here.

class Sector(models.Model):
    sector_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100,blank=True)

    def __str__(self) -> str:
        return self.sector_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.sector_name.replace('ı','i').replace('ə','e').replace('ö','o').replace('ü','u'))
            
        return super().save(*args, **kwargs)
    
class Subsector(models.Model):
    subsector_name = models.CharField(max_length=150)
    sector = models.ForeignKey('app.Sector', on_delete=models.CASCADE, related_name='sub_sectors')
    slug = models.SlugField(max_length=100,blank=True)

    def __str__(self) -> str:
        return self.subsector_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.subsector_name.replace('ı','i').replace('ə','e').replace('ö','o').replace('ü','u'))
            
        return super().save(*args, **kwargs)
    
class Indicator(models.Model):
    indicator_name = models.CharField(max_length=150)
    sub_sector = models.ForeignKey('app.Subsector', on_delete=models.CASCADE, related_name='indicators')
    content = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(max_length=100,blank=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug=slugify(self.indicator_name.replace('ı','i').replace('ə','e').replace('ö','o').replace('ü','u'))
            
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.indicator_name

    
class Profile(models.Model):
    name = models.CharField(max_length=100)
    data = models.JSONField()