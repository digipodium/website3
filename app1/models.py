from django.db import models

# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=160,null=False)
    description = models.TextField(default="No description")

    def __repr__(self):
        return self.headline
    
    def __str__(self):
        return self.headline


class Note(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

