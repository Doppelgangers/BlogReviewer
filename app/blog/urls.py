from django.urls import path , include
from .views import *

urlpatterns = [
    path('', Posts_all.as_view() , name = 'home' ),

    path('registration/', Registration.as_view() , name = 'reg' ),
    path('authorization/', Authorization.as_view() , name = 'aut' ),
    path('logout/', logout_user , name = 'logout' ),

    path('category/<str:slug_category>', Posts_by_category.as_view() , name = 'posts_by_category' ),

    path('detail/post/<str:slug_post_detail>', Post_detail.as_view() , name = 'post_detail' ),
    path('detail/author/<str:slug_author_detail>', Author_detail.as_view() , name = 'author_detail' ),
    path('detail/genre/<str:slug_genre_detail>', Author_detail.as_view() , name = 'genre_detail' ),

]

