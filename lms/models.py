from django.db import models
from config import settings

# from users.models import User

# Create your models here.

class Course(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='lms/', blank=True, null=True, verbose_name='Превью')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Владелец')
    last_change = models.DateTimeField(blank=True, null=True, verbose_name='Время последнего изменения')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Lesson(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='lms/', blank=True, null=True, verbose_name='Превью')
    video_link = models.CharField(max_length=500, blank=True, null=True, verbose_name='Ссылка на видео')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Описание')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name

class Subscription(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)

