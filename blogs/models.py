from django.db import models

# Create your models here.
class Post(models.Model):
    #Model a blog post
    title = models.CharField()
    body =models.TextField()
    author = models.CharField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        #String representation of Post object
        return self.title