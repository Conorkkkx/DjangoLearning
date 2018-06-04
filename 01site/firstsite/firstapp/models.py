from django.db import models

# Create your models here.
class People(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(null = True, blank = True, max_length=200)
    job = models.CharField(null = True, blank = True, max_length=200)

class Article(models.Model):
    TAG_CHOICES = (
        ('tech', 'Tech'),
        ('life', 'Life'),
    )
    headline = models.CharField(null=True, blank=True, max_length=500)
    content = models.TextField(null=True, blank=True)
    tag = models.CharField(null=True, blank=True, max_length=5, choices=TAG_CHOICES)
    def __str__(self):
        return self.headline

class Comment(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    comment = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.comment
