from django.urls import path
from .views import CreateAccountView, UserProfileView, AuthorView

app_name = 'users'

urlpatterns = [
    path('create-account/', 
    CreateAccountView.as_view(), 
    name='create-account'),
    path('<int:pk>/', UserProfileView.as_view(), name = "user_profile"),
    path('author/<int:pk>/', AuthorView.as_view(), name = "author_profile")
]