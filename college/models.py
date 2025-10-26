from django.db import models
from users.models import User


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    preview = models.ImageField(
        upload_to="courses/preview",
        verbose_name="Превью курса",
        help_text="Загрузите картинку",
        blank=True,
        null=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
    )
    owner = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Урок",
        help_text="Укажите название урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Название курса",
        help_text="Укажите название курса",
        blank=True,
        null=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
    )
    preview = models.ImageField(
        upload_to="lesson/preview",
        verbose_name="превью урока",
        help_text="Загрузите картинку урока",
        blank=True,
        null=True,
    )
    url_video = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Подписчик', related_name='subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='subscriptions')

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
