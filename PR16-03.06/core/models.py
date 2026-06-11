from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """
    Книга в мобильном приложении BookTracker.
    Каждая книга принадлежит одному пользователю.
    """

    STATUS_CHOICES = [
        ('want', 'Хочу прочитать'),
        ('reading', 'Читаю'),
        ('done', 'Прочитана'),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Владелец'
    )

    title = models.CharField(
        max_length=200,
        verbose_name='Название книги'
    )

    author = models.CharField(
        max_length=150,
        verbose_name='Автор'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='want',
        verbose_name='Статус'
    )

    rating = models.IntegerField(
        default=0,
        verbose_name='Оценка'
    )

    started = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата начала чтения'
    )

    finished = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата завершения'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.owner.username}: {self.title}'