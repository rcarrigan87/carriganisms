from django.db import models
from django.contrib.auth.models import User


"""
class PublishedManager(models.Manager):
    #return published only
    #return recently published

class PostViewManager(models.Manager):
    #return most viewed posts
"""
class Category(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    cat_slug = models.SlugField(max_length=128, blank=False)
    description = models.CharField(max_length=180, blank=True, help_text="Further describe this category")

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=128, blank=False)
    category = models.ManyToManyField(Category, blank=True)
    author = models.ForeignKey(User, blank=True)
    slug = models.SlugField(max_length=128, blank=False)
    description = models.CharField(max_length=180, help_text="meta tag and previews") 
    content = models.TextField(blank=True)
    focus_keyword = models.CharField(max_length=180, help_text="Page Target Keyword", blank=True)
    
    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_CHOICES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    )

    status = models.CharField(max_length=128, choices=STATUS_CHOICES)
    pub_date = models.DateField(help_text="Publish Date", blank=True, null=True)
    main_image = models.URLField(help_text="http://placehold.it/900x300", blank=True, max_length=128)
    main_image_alt = models.CharField(max_length=50, help_text="Image description tag", blank=True) 
    og_image = models.URLField(help_text="Image for Facebook OpenGraph; Min 200x200", blank=True, max_length=128)
    og_image_alt = models.CharField(max_length=50, help_text="Image description tag", blank=True) 
    views = models.IntegerField(default=0) 

    objects = models.Manager()

    #def seo_check(self):
        

    def __unicode__(self):
        return self.title

