import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from slugify import slugify

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_slug = models.SlugField(max_length=200, default="", blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.cat_slug = slugify(self.cat_name)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.cat_name

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
	(2, "Future"),
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default="", blank=True, unique=True)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, blank=True, on_delete= models.CASCADE,related_name='blog')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_on <= now
        was_published_recently.admin_order_field = '-created_on'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Yayınlanma?'
    def __str__(self):
        return self.title