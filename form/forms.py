from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="Nombre", widget=forms.TextInput(
        attrs={'class': 'feedback-input', 'placeholder': 'Escriba su nombre'}))
    email = forms.EmailField(label = "Correo electrónico", widget=forms.EmailInput(
        attrs={'class': 'feedback-input', 'placeholder': 'Escriba su email'}))
    text = forms.CharField(label="Mensaje", widget=forms.TextInput(
        attrs={'class': 'feedback-input', 'placeholder': 'Escriba su mensaje'}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'text']
        