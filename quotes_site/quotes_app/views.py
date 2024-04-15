from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import QuoteForm  # Імпортуємо форму для додавання цитати
from .models import Quote  # Імпортуємо модель цитати


def register(request):
    # Обробка запитів методом POST для реєстрації користувача
    if request.method == 'POST':
        # Створення форми реєстрації з POST-даними
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Збереження нового користувача, якщо дані введено коректно
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Автентифікація користувача після реєстрації
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                # Повідомлення про успішну реєстрацію та вхід
                messages.success(
                    request, 'Реєстрація пройшла успішно. Ви увійшли в систему.')
                # Перенаправлення на домашню сторінку після входу
                return redirect('home')
        else:
            # Обробка помилок, якщо дані форми некоректні
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            # Перенаправлення на сторінку реєстрації у разі помилки
            return redirect('register')
    else:
        # Передача порожньої форми реєстрації для відображення
        form = UserCreationForm()
    # Відображення сторінки реєстрації з формою
    return render(request, 'quotes_app/register.html', {'form': form})


def add_quote(request):
    # Перевірка, чи користувач залогінений перед тим, як додати нову цитату
    if not request.user.is_authenticated:
        # Якщо користувач не залогінений, перенаправлення на сторінку входу
        return redirect('login')
    if request.method == 'POST':
        # Створення форми для додавання цитати з POST-даними
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Збереження цитати, якщо дані введено коректно
            quote = form.save(commit=False)
            quote.author = request.user  # Встановлення автора цитати на поточного користувача
            quote.save()
            # Повідомлення про успішне додавання цитати
            messages.success(request, 'Цитата успішно додана.')
            # Перенаправлення на домашню сторінку після додавання цитати
            return redirect('home')
    else:
        # Передача порожньої форми для введення нової цитати
        form = QuoteForm()
    # Відображення сторінки з формою для додавання цитати
    return render(request, 'quotes_app/add_quote.html', {'form': form})
