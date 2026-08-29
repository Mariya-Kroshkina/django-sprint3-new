from django.db import models


class CreateBaseModel(models.Model):
    """Абстрактная модель для даты создания записи"""

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True


class PublishBaseModel(models.Model):
    """Абстрактная модель для состояния публикации"""

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        abstract = True
