from django.contrib import admin
from .models import NewsStory
from .models import Category

admin.site.register(Category)

admin.site.register(NewsStory)

