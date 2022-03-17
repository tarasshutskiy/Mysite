from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
from config import settings


class Category(models.Model):
    """Категорії"""
    name = models.CharField('Категорія', max_length=35)
    slug = models.SlugField('Slug', max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Post(models.Model):
    """Модель для поста"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автор')
    name = models.CharField("Пост", max_length=35)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    description = models.TextField('Описання', blank=True)
    description_cod = models.TextField('Описання коду', blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категорія"
    )
    time_create = models.DateTimeField("Дата і час створення", auto_now_add=True)
    time_update = models.DateTimeField("Дата і час публікації", auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='Публікація')

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='comments'
    )
    comment = models.CharField(max_length=150, verbose_name='Коментар')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    time_create = models.DateTimeField("Дата і час створення", auto_now_add=True)

    class Meta:
        verbose_name = "Коментарій"
        verbose_name_plural = "Коментарі"

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('post_list')
