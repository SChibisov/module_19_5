from django.http import *
from django.shortcuts import render
from .forms import UserRegister
from .models import Flowers, Buyer


def flowers_shop(request):
    return render(request, "main.html")


def shop(request):
    header = 'Магазин цветов'
    button = 'Добавить в корзину'
    flowers = Flowers.objects.all()
    data = {"header": header, "button": button, "flowers": flowers}
    return render(request, "shop.html", context=data)


def cart(request):
    return render(request, "shopping_cart.html")


def sign_up_by_html(request):
    info = {}
    users = Buyer.objects.all()
    users_list = [buyer.name for buyer in users]
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username not in users_list and password == repeat_password and int(age) >= 18:
            Buyer.objects.create(name=username, age=age)
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            if username in users_list:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
    form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info})


def sign_up_by_django(request):
    info = {}
    users = Buyer.objects.all()
    users_list = [buyer.name for buyer in users]
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in users_list and password == repeat_password and age >= 18:
                Buyer.objects.create(name=username, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
            else:
                if username in users_list:
                    info['error'] = 'Пользователь уже существует'
                elif password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif age < 18:
                    info['error'] = 'Вы должны быть старше 18'
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info})