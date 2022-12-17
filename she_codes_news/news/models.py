from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class NewsStory(models.Model):
    class Meta:
        ordering = ['-pub_date']
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(blank=True)
   



  
 