from django.db import models


class Report(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ваше имя')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.created_at.strftime("%d.%m.%Y")}'

    @property
    def photo(self):
        """
        Обратная совместимость со старыми шаблонами: report.photo.url
        отдаёт первое фото отчёта.
        """
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