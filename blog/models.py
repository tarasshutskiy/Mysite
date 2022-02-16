from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    """Категорії"""
    name = models.CharField('Категорія', max_length=100)
    description = models.TextField('Описання')
    slug = models.SlugField('Slug', max_length=200, unique=True)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('post_list_view', kwargs={'slug': self.slug})


class Post(models.Model):
    """Модель для поста"""
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    name = models.CharField("Пост", max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
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
        return reverse('post_detail_view', kwargs={'category': self.category.slug, 'slug': self.slug})



class Comment(models.Model):
    name = models.CharField("Коментарій", max_length=100)
    email = models.CharField('Пошта', max_length=100)
    website = models.CharField('Сайт', max_length=100)
    message = models.TextField('Повідомлення', max_length=500)
    post = models.ForeignKey(
        Post,
        related_name='comment',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )


    class Meta:
        verbose_name = "Коментарій"
        verbose_name_plural = "Коментарії"

    def __str__(self):
        return self.name
