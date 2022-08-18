from django.db import models
from django.contrib.auth.models import User
class Artwork (models.Model):

    title = models.CharField(max_length=255 , verbose_name='Название')
    image = models.ImageField( upload_to="photos/%Y/%m/%d/", verbose_name='Обложка'  , null=True )
    year  = models.IntegerField(max_length=4 ,  verbose_name="Год" , blank=True , null=True )
    estimatio = models.IntegerField(max_length=1 , verbose_name="Оценка" , blank=True  , null=True)
    description = models.TextField( blank=True , verbose_name="Описание")
    review = models.TextField( blank=True , verbose_name="Отзыв")

    author = models.ForeignKey('Author' , models.SET_NULL , verbose_name='Автор' ,blank=True , null=True )
    category = models.ForeignKey('Category' , models.PROTECT , verbose_name='Категория')
    genre  = models.ManyToManyField('Genre' ,  verbose_name="Жанры" ,blank=True , null=True)
    series = models.ForeignKey('Series' , models.PROTECT , verbose_name="Серия" , blank=True, null=True)
    creator = models.ForeignKey(User , models.SET_NULL , verbose_name='Автор записи' , blank=True , null=True )
    views = models.ManyToManyField("Ip", related_name="post_views", blank=True)

    data_end_look = models.DateTimeField(auto_now_add=True , verbose_name='Дата просмотра' , blank=True )
    data_create = models.DateTimeField(auto_now_add=True , verbose_name="Дата публикации записи" , blank=True)
    slug  = models.SlugField( verbose_name="URL" , unique=True , db_index=True , blank=True)

    def total_views(self):
        return self.views.count()

class Category (models.Model):
    title = models.CharField(max_length=255 , verbose_name='Название')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)

class Genre (models.Model):
    title = models.CharField(max_length=255 , verbose_name='Название')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)
    description = models.CharField(max_length=1_000, null=True, verbose_name="Описание")

class Series (models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)

class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя/Псевданим')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)
    image = models.ImageField(upload_to="authors/", verbose_name='Обложка', null=True , blank=True)
    content = models.TextField(verbose_name='Информаия о авторе',null=True,blank=True)

    class Ip(models.Model):  # наша таблица где будут айпи адреса
        ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip
