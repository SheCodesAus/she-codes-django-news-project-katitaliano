from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from news.models import NewsStory
from .models import CustomUser
from .forms import CustomUserCreationForm


class CreateAccountView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/create_account.html'

class UserAccountView(generic.DetailView):
	model = CustomUser
	template_name = 'users/user_account_detail.html'
	context_object_name = 'user'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
		return context

class AuthorView(generic.DetailView):
	model = CustomUser
	template_name = 'users/author_profile_detail.html'
	context_object_name = 'author'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
		return context

