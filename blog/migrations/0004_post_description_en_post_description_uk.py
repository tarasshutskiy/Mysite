# Generated by Django 4.0.2 on 2022-03-21 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='post',
            name='description_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
