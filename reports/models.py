from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ваше имя')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='reports/', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.created_at.strftime("%d.%m.%Y")}'
