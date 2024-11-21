from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(label='Введите логин', max_length=30,
                               help_text='Логин не должен быть длиннее 30 символов', required=True)
    password = forms.CharField(label='Введите пароль', min_length=8,
                               help_text='Пароль должен быть не менее 8 символов', required=True)
    repeat_password = forms.CharField(label='Повторите пароль', min_length=8, required=True)
    age = forms.IntegerField(label='Введите свой возраст', min_value=1, max_value=100,
                             help_text='Значение не должно быть больше 3 символов', required=True)
