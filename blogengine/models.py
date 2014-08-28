from django.db import models

# Create your models here.

class Post():
	title = models.CharField(max_length=100)
	author = models.ForeignKey(User)
	slug = models.SlugField(max_length=100)
	description = models.TextField(help_text=("meta tag and previews"))
    content = models.TextField()


	main_image = models.URLField(help_text=("Image for post banner, size TBD"), null=True, blank=True)


	og_image = models.URLField(help_text=("Image for Facebook OpenGraph; Min 200x200"), null=True, blank=True)
	
	#add in google authorship rich snippets tag


	class Meta:
		ordering = 

class Category():

class User(): #django apparently has built in user model...


class Post(TimeStampedModel):

    STATUS_DRAFT = "draft"
    STATUS_PUBLISHED = "published"
    STATUS_CHOICES = (
        (STATUS_DRAFT, _(STATUS_DRAFT)),
        (STATUS_PUBLISHED, _(STATUS_PUBLISHED)),
    )

    objects = PostManager()
    tags = TaggableManager()

    title = models.CharField(_("Title"), max_length=100)
    slug = models.SlugField(_("Slug"), max_length=100)
    keywords = models.TextField(_("META Keywords"))
    description = models.TextField(_("Short description"), help_text=_("For headers/rss and quick page info feed"))
    status = models.CharField(_("Status"), max_length=20, choices=STATUS_CHOICES)
    lead_image = models.URLField(_("Lead image URL"), help_text=_("Point at a lead image which will be featured in Facebook OpenGraph."), null=True, blank=True)
    body = models.TextField()
    pub_date = models.DateField()

    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-pub_date', ]
        get_latest_by = 'pub_date'