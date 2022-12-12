from django.urls import path
from .views import CreateAccountView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', 
    CreateAccountView.as_view(), 
    name='createAccount'),
    path('<int:pk>/', UserProfileView.as_view(), name = "user")
]