from django.shortcuts import render, redirect
from django.urls import path, include
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Визначення функції для додавання автора


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

# Визначення функції для додавання цитати


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})

# Визначення функції для відображення всіх цитат


def all_quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'all_quotes.html', {'quotes': quotes})

# Вигляд для домашньої сторінки


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

# Вигляд для реєстрації користувача


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def author_detail_view(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'author_detail.html', {'author': author})
