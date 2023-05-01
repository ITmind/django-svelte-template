from django.db import models
from django.utils.text import slugify


class Notes(models.Model):
    date = models.DateField(primary_key=True, verbose_name="date published")
    title = models.CharField(max_length=200)
    note = models.CharField(max_length=2000)
    slug = models.SlugField(editable=False, unique=True)

    # def __str__(self):
    #     return f'{self.date}: {self.title}'

    def save(self, *args, **kwargs):
        to_slug = f"{self.date}-{self.title}"
        self.slug = slugify(to_slug)
        super().save(*args, **kwargs)
