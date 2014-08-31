from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

"""
class PublishedManager(models.Manager):
    #return published only
    #return recently published

class PostViewManager(models.Manager):
    #return most viewed posts
"""
class Category(models.Model):
    name = models.CharField(max_length=32, primary_key=True)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=128, blank=False)
    category = models.ForeignKey(Category, blank=True)
    author = models.ForeignKey(User, blank=True)
    slug = models.SlugField(max_length=128, blank=False)
    description = models.CharField(max_length=180, help_text="meta tag and previews") 
    content = models.TextField(blank=True)
    
    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_CHOICES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    )

    status = models.CharField(max_length=128, choices=STATUS_CHOICES)
    pub_date = models.DateField()
    main_image = models.URLField(help_text="Image for post banner, size TBD", blank=True, max_length=128)
    og_image = models.URLField(help_text="Image for Facebook OpenGraph; Min 200x200", blank=True, max_length=128)
    views = models.IntegerField(default=0) 
    #http://stackoverflow.com/questions/1603340/track-the-number-of-page-views-or-hits-of-an-object

    objects = models.Manager()

    #custom manager for blog posts
    #published_post = PublishedManager() 
    #viewed_post = PostViewManager()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title

