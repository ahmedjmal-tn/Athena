# Generated by Django 4.1.7 on 2023-05-29 15:59

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(verbose_name='Series slug')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
            ],
            options={
                'verbose_name_plural': 'Series',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('article_slug', models.SlugField(unique=True, verbose_name='Article slug')),
                ('content', ckeditor.fields.RichTextField(blank=True, default='')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date modified')),
                ('etat', models.CharField(choices=[('accepted', 'accepted'), ('refused', 'refused'), ('panding', 'panding')], default='panding', max_length=20)),
                ('image', models.ImageField(upload_to='article_images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('series', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='Article.articleseries', verbose_name='Series')),
            ],
            options={
                'verbose_name_plural': 'Article',
                'ordering': ['-published'],
            },
        ),
    ]
