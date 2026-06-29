from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'description', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя или ник',
                'class': 'form-input'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Расскажите о вашей кормушке: где установили, что видели...',
                'rows': 4,
                'class': 'form-textarea'
            }),
            'photo': forms.FileInput(attrs={
                'accept': 'image/*',
                'class': 'form-file'
            }),
        }
        labels = {
            'name': 'Ваше имя',
            'description': 'Описание',
            'photo': 'Фото кормушки',
        }
