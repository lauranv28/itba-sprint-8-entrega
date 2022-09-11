from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    dni=forms.IntegerField(label='DNI', required=True)
    email= forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    #Cliente o empleado
    coe = forms.CharField(label='¿Es Cliente o Empleado?', max_length=10)
    
    class Meta:
        model = User
        fields = ['username', 'dni','email','password1','password2', 'coe']
        help_texts={k:"" for k in fields}
