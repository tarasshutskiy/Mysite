from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
from config import settings


class Category(models.Model):
    """Категорії"""
    name = models.CharField('Category', max_length=35)
    slug = models.SlugField('Slug', max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Post(models.Model):
    """Модель для поста"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Author')
    name = models.CharField("Post", max_length=35)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    description = models.TextField('Description', blank=True)
    description_cod = models.TextField('Description code', blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Category"
    )
    time_create = models.DateTimeField("Date and time of creation", auto_now_add=True)
    time_update = models.DateTimeField("Date and time of last update", auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='Publication')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        verbose_name='Post',
        related_name='comments'
    )
    comment = models.CharField(max_length=150, verbose_name='Comment')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author',
    )
    time_create = models.DateTimeField("Date and time of creation", auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('post_list')
