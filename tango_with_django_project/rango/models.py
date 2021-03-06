from __future__ import unicode_literals
import datetime
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    view = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)
        if self.view<0:
            self.view=0

        
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self): # For Python 2, use __unicode__ too
        return self.name
    
class Page(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self): # For Python 2, use __unicode__ too
        return self.title
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    def __str__(self):
        return self.user.username
