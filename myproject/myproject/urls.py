from django.urls import path, include
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView  # Додано TemplateView
from myapp.forms import AuthorForm, QuoteForm
from myapp.models import Author, Quote
from django.shortcuts import render
from myapp.views import HomeView, add_author, add_quote, all_quotes, SignUpView

# Шляхи URL
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(
        form_class=UserCreationForm,
        success_url=reverse_lazy('login'),
        template_name='registration/signup.html'
    ), name='signup'),
    path('add_author/', add_author, name='add_author'),
    path('add_quote/', add_quote, name='add_quote'),
    path('authors/', ListView.as_view(
        model=Author,
        template_name='author_list.html',
        context_object_name='authors'
    ), name='author_list'),
    path('authors/', DetailView.as_view(
        model=Author,
        template_name='author_detail.html',
        context_object_name='author'
    ), name='author_detail'),
    path('all_quotes/', all_quotes, name='all_quotes'),
]
