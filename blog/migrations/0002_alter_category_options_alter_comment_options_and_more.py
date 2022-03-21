# Generated by Django 4.0.2 on 2022-03-20 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=35, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=150, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date and time of creation'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description_cod',
            field=models.TextField(blank=True, verbose_name='Description code'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publication'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=35, verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date and time of creation'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_update',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date and time of last update'),
        ),
    ]
