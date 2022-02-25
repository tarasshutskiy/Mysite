from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    """Категорії"""
    name = models.CharField('Категорія', max_length=100)
    slug = models.SlugField('Slug', max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('categories', kwargs={'category_slug': self.slug})




class Post(models.Model):
    """Модель для поста"""
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    name = models.CharField("Пост", max_length=100)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    image_post = models.ImageField('Зображення поста', upload_to='image_post/')
    image_cod = models.ImageField('Зображення коду', upload_to='image_cod/')
    image_res = models.ImageField('Зображення результату', upload_to='image_res/')
    description = models.TextField('Описання')
    description_cod = models.TextField('Описання коду')
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True,
    )
    time_create = models.DateTimeField("Дата і час створення", auto_now_add=True)
    time_update = models.DateTimeField("Дата і час публікації", auto_now_add=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('posts', kwargs={'post_slug': self.slug})




