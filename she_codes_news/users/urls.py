from django.urls import path
from .views import CreateAccountView, UserAccountView, AuthorView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='create-account'),
    path('<int:pk>/', UserAccountView.as_view(),name='user_account'),
    path('author/<int:pk>/', AuthorView.as_view(), name = 'author_profile'),
]

