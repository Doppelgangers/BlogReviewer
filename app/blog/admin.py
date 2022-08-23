from django.contrib import admin

from .models import *

class Artwork_Admin(admin.ModelAdmin):
    list_display = ('title' , 'year' , 'category' , 'creator','data_end_look')
    list_display_links = ( 'title' , 'year' )
    search_fields = ( 'title' , 'year' )
    # list_editable =
    list_filter = ( 'series' ,'data_end_look')
    prepopulated_fields = {'slug': ('title' ,) }

class Category_Admin(admin.ModelAdmin):
    list_display = ('title' , 'slug')
    # list_display_links =
    # search_fields =
    # list_editable =
    # list_filter =
    prepopulated_fields = {'slug': ('title' ,) }

class Genre_Admin(admin.ModelAdmin):
    list_display = ("title" , "slug" , 'description')
    # list_display_links =
    # search_fields =
    # list_editable =
    # list_filter =
    prepopulated_fields = {'slug': ('title' ,) }

class Series_Admin(admin.ModelAdmin):
    list_display = ('title' , 'slug')
    # list_display_links =
    # search_fields =
    # list_editable =
    # list_filter =
    prepopulated_fields = {'slug': ('title' ,) }

class Author_Admin(admin.ModelAdmin):
    list_display = ('name' ,'name' , 'content')
    # list_display_links =
    # search_fields =
    # list_editable =
    # list_filter =
    prepopulated_fields = {'slug': ('name' ,) }


admin.site.register(Artwork , Artwork_Admin)
admin.site.register(Category , Category_Admin)
admin.site.register(Genre , Genre_Admin)
admin.site.register(Series , Series_Admin)
admin.site.register(Author , Author_Admin)
admin.site.register(Ip)








# Register your models here.
