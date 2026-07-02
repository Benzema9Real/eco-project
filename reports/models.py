import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

CYRILLIC_TO_LATIN = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
    'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
}


def transliterate(text):
    result = []
    for char in text.lower():
        if char in CYRILLIC_TO_LATIN:
            result.append(CYRILLIC_TO_LATIN[char])
        else:
            result.append(char)
    return ''.join(result)


class Report(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ваше имя')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.created_at.strftime("%d.%m.%Y")}'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(transliterate(self.name)) or 'otchet'
            self.slug = f'{base}-{uuid.uuid4().hex[:6]}'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('report_detail', args=[self.slug])

    @property
    def photo(self):
        first = self.photos.first()
        return first.image if first else None


class ReportPhoto(models.Model):
    report = models.ForeignKey(Report, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reports/', verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото отчёта'
        verbose_name_plural = 'Фото отчётов'

    def __str__(self):
        return f'Фото для отчёта #{self.report_id}'