from django.contrib.auth.models import User
from django.db import models




class NewsModel(models.Model):
    """
    News model
    """
    name = models.CharField(max_length=100, blank=False, null=False, default='Unnamed', verbose_name='News name')
    text = models.TextField(blank=False, verbose_name='News text')
    created = models.DateTimeField(auto_now_add=True, verbose_name='News created')
    updated = models.DateTimeField(auto_now=True, verbose_name='News updated')
    published = models.BooleanField(default=False, verbose_name='Published')
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
