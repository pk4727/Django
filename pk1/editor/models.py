from django.db import models

# Create your models here.
from tinymce.models import HTMLField
from autoslug import AutoSlugField
class editor_news(models.Model):
    news_title = models.CharField(max_length=225)
    news_desc = HTMLField()
    news_slug = AutoSlugField(populate_from='news_title',unique=True,null=True,default=None)  # sluge field
    news_img = models.FileField(upload_to="news/",max_length=250,null=True, default=None)  # for media upload