from django import forms
from django.forms import ModelForm
from .models import NewsStory
from .models import Category

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image_url', 'category', 'content']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
            }
