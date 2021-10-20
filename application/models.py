from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    """Публикация постов"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def save(self, *args, **kwargs):
        if not self.title:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'


class Song(models.Model):
    """ MP3/MP4 файлы"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    name = models.TextField(verbose_name='Название')
    audio_file = models.FileField(blank=True, null=True, verbose_name='Аудио файл')
    audio_link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ссылка')
    duration = models.CharField(max_length=20, verbose_name='Длительность')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    paginate_by = 6

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио'


class Video(models.Model):
    """Видио"""
    # search_fields = ('title',)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    name = models.CharField(max_length=500, verbose_name='Название Видио')
    file = models.FileField(upload_to='videos/', null=True, verbose_name="Видио файл")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    paginate_by = 6

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видио'
        verbose_name_plural = 'Видио'


