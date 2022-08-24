from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
class Artwork (models.Model):

    title = models.CharField(max_length=255 , verbose_name='Название')
    english_title = models.CharField(max_length=255 , verbose_name='Англиское название' , blank=True , null=True)
    image = models.ImageField( upload_to="photos/%Y/%m/%d/", verbose_name='Обложка'  , null=True )
    year = models.IntegerField(  verbose_name="Год" , blank=True , null=True )
    estimatio = models.IntegerField(verbose_name="Оценка" , blank=True  , null=True)
    description = models.TextField( blank=True , verbose_name="Описание")
    review = models.TextField( blank=True , verbose_name="Отзыв")

    number = models.IntegerField(verbose_name="Номер тома или сезона" , null=True , blank=True)

    author = models.ForeignKey('Author' , models.SET_NULL , verbose_name='Автор' ,blank=True , null=True )
    category = models.ForeignKey('Category' , models.PROTECT , verbose_name='Категория')
    genre  = models.ManyToManyField('Genre' ,  verbose_name="Жанры" ,blank=True )
    series = models.ForeignKey('Series' , models.PROTECT , verbose_name="Серия" , blank=True, null=True)
    creator = models.ForeignKey(User , models.SET_NULL , verbose_name='Автор записи' , blank=True , null=True )
    views = models.ManyToManyField("Ip", related_name="post_views", blank=True)

    data_end_look = models.DateTimeField(auto_now_add=True , verbose_name='Дата просмотра' , blank=True )
    data_create = models.DateTimeField(auto_now_add=True , verbose_name="Дата публикации записи" , blank=True)
    slug  = models.SlugField( verbose_name="URL" , unique=True , db_index=True , blank=True)
    is_active = models.BooleanField( default=True )
    def get_absolute_url(self):
        return reverse('post_detail' , kwargs={'slug_post_detail':self.slug} )

    def total_views(self):
        return self.views.count()

    class Meta:
        ordering = ['-data_end_look']

class Category (models.Model):
    title = models.CharField(max_length=255 , verbose_name='Название')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)

    def get_posts_by_category(self):
        return reverse('posts_by_category' , kwargs={'slug_category' : self.slug})

    def __str__(self):
        return self.title

class Genre (models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)
    description = models.CharField(max_length=1_000, null=True, verbose_name="Описание")

    def get_detail_ganre(self):
        return reverse('genre_detail' , kwargs={'slug_genre_detail' : self.slug})

    def __str__(self):
        return self.title

class Series (models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя/Псевданим')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)
    image = models.ImageField(upload_to="authors/", verbose_name='Обложка', null=True , blank=True)
    content = models.TextField(verbose_name='Информаия о авторе',null=True,blank=True)
    def get_absolute_url(self):
        return reverse('author_detail' , kwargs={'slug_author_detail':self.slug} )

    def __str__(self):
        return self.name

class Ip(models.Model):  # наша таблица где будут айпи адреса
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Image_Artwork(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images_artwork/", verbose_name='Снимоок')