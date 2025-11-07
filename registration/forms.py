from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """用户注册表单"""

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'})
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'gender', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            if field_name == 'gender':
                field.widget.attrs.update({'class': 'form-select'})


class LoginForm(forms.Form):
    """登录表单"""
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '请输入用户名'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '请输入密码'
        })
    )