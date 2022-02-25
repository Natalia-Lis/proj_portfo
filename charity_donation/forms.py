from django.core.exceptions import ValidationError
from .models import Category, Institution, Donation
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django import forms


def validate_email(value):
    """ Check database before sending email for password reset """
    try:
        User.objects.get(email=value)
    except:
        raise ValidationError("Nie ma takiego użytkownika")


class MyCustomResetForm(PasswordResetForm):
    email = forms.EmailField(label=("Email"), max_length=254, validators=[validate_email])


# class CustomForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = ('username', 'first_name', 'last_name', "password1", "password2")


# def validate_passwords(password1,password2):
#     sp_characters = "[!#$%&'()*+,-./:;<=>?@'[\]^_`{|}\"~]"
#     if password1!=password2:
#         raise ValidationError("Hasła się nie zgadzają.")
#     if len(password1) < 8:
#         raise ValidationError('Hasło musi mieć minimum 8 znaków.')
#     if not any(char.isdigit() for char in password1):
#         raise ValidationError('Hasło musi zawierać minimum jedną cyfrę.')
#     if not any(char.islower() for char in password1):
#         raise ValidationError('Hasło musi zawierać przynajmniej 1 małą literę.')
#     if not any(char.isupper() for char in password1):
#         raise ValidationError('Hasło musi zawierać przynajmniej 1 dużą literę.')
#     if not any(char in sp_characters for char in password1):
#         raise ValidationError('Hasło musi zawierać przynajmniej 1 znak specjalny. '+sp_characters)


class EditPassword(forms.Form):
    old_password1 = forms.CharField(max_length=64, widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=64, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=64, widget=forms.PasswordInput)

