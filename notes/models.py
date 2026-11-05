from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes", verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def __str__(self):
        return self.title
