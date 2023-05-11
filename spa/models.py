from django.db import models
from django.utils.text import slugify


class Notes(models.Model):
    date = models.DateField(primary_key=True, verbose_name="date published")
    title = models.CharField(max_length=200)
    note = models.CharField(max_length=2000)
    # Данный атрибут нужен для переходов по url к конкретной записи.
    # Если бы у нас primary key был например int, то slug можно было не делать
    slug = models.SlugField(editable=False, unique=True)

    def __str__(self):
        """
        Возвращает представление экземпляра класса
        :return:
        """
        return f'{self.date}: {self.title}'

    def save(self, *args, **kwargs):
        """
        Перехват записи экземпляра класса.
        Нужен для формирования slug
        """
        to_slug = f"{self.date}-{self.title}"
        self.slug = slugify(to_slug)
        super().save(*args, **kwargs)
