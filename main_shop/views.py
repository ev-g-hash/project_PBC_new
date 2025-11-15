# main_shop/views.py
import requests
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def index(request):
    return render(request, 'shop/index.html')


def aboutas(request):
    return render(request, 'shop/aboutas.html')


def readmore(request):
    return render(request, 'shop/readmore.html')


def forms(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Данные формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Отправка в Telegram
            BOT_TOKEN = '8581138752:AAEyEJWYZrjo0GjdKowbIk23tA9k7qDr0oY'
            CHAT_ID = '443467930'
            TELEGRAM_API = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
            
            telegram_message = f"""Вам новая заявка:
Имя: {name}
Email: {email}
Телефон: {phone}
Сообщение: {message}"""

            try:
                requests.post(TELEGRAM_API, data={
                    'chat_id': CHAT_ID,
                    'text': telegram_message
                })
            except Exception as e:
                print(f"Ошибка отправки в Telegram: {e}")

            # Возвращаем сообщение пользователю
            return HttpResponse("Ожидайте в ближайшее время мы с вами свяжемся!")
    else:
        form = ContactForm()
    
    return render(request, 'shop/forms.html', {'form': form})
