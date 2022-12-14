# Generated by Django 4.1 on 2022-08-22 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя/Псевданим')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='authors/', verbose_name='Обложка')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Информаия о авторе')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('description', models.CharField(max_length=1000, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Обложка')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год')),
                ('estimatio', models.IntegerField(blank=True, null=True, verbose_name='Оценка')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('review', models.TextField(blank=True, verbose_name='Отзыв')),
                ('data_end_look', models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')),
                ('data_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации записи')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='URL')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.author', verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='Категория')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор записи')),
                ('genre', models.ManyToManyField(blank=True, to='blog.genre', verbose_name='Жанры')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.series', verbose_name='Серия')),
                ('views', models.ManyToManyField(blank=True, related_name='post_views', to='blog.ip')),
            ],
        ),
    ]
