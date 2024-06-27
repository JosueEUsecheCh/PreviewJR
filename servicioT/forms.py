from django import forms
from phonenumber_field.formfields import PhoneNumberField

class Contactanos(forms.Form):
    asunto = forms.CharField(label='Caso', max_length=150)
    exposicion = forms.CharField(label='Asunto', widget=forms.Textarea)
    email = forms.EmailField(label='Correo Electrónico',required=True)  # Agrega el campo de correo electrónico