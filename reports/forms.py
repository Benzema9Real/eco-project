from django import forms
from .models import Report

MAX_PHOTOS = 12


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ReportForm(forms.ModelForm):
    photos = MultipleFileField(
        label='Фото кормушки (до 12 штук)',
        required=True,
        widget=MultipleFileInput(attrs={
            'accept': 'image/*',
            'multiple': True,
            'class': 'form-file',
        }),
    )

    class Meta:
        model = Report
        fields = ['name', 'description']
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
        }
        labels = {
            'name': 'Ваше имя',
            'description': 'Описание',
        }

    def clean_photos(self):
        photos = self.cleaned_data.get('photos') or []
        if not photos:
            raise forms.ValidationError('Загрузите хотя бы одно фото.')
        if len(photos) > MAX_PHOTOS:
            raise forms.ValidationError(f'Можно загрузить не больше {MAX_PHOTOS} фото за раз.')
        return photos