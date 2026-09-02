from django.contrib.auth import get_user_model
from django.db import models


CHARFIELD_MAX_LENGTH = 256
ADMIN_TITLE_MAX_LENGTH = 20


User = get_user_model()


class BaseModel(models.Model):
    """Абстрактная модель для даты создания записи и публикации"""

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        abstract = True


class Location(BaseModel):
    name = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        verbose_name='Название места'
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name[:ADMIN_TITLE_MAX_LENGTH]


class Category(BaseModel):
    title = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        verbose_name='Заголовок'
    )
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; разрешены символы '
            'латиницы, цифры, дефис и подчёркивание.'
        )
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:ADMIN_TITLE_MAX_LENGTH]


class Post(BaseModel):
    title = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        verbose_name='Заголовок'
    )
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем — '
            'можно делать отложенные публикации.'
        )
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='posts_author'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение',
        related_name='posts_location'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='posts_category'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title[:ADMIN_TITLE_MAX_LENGTH]
