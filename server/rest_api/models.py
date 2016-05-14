from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


class Platform(models.Model):
    name = models.CharField(max_length=50)
    # Use FileField instead of ImageField so it allows svg format
    icon = models.FileField(upload_to='icons/platforms/')
    url = models.URLField()

    def __str__(self):
        return self.name


class WorkPiece(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    platform = models.ForeignKey(Platform, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    color = models.CharField(
        max_length=7,
        default='#FFFFFF',
        validators=[RegexValidator(
            regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
            message='Color must be in hex format'
        )]
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class App(WorkPiece):
    store_url = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ('-start_date',)


class Repo(WorkPiece):
    subtitle = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)


class Article(WorkPiece):
    publish_date = models.DateField()

    class Meta:
        ordering = ('-publish_date',)
