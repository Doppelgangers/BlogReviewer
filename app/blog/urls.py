from django.urls import path , include
from .views import *

urlpatterns = [
    path('', index , name = 'home' ),
    path('', index , name = 'author_detail' ),
    path('registration/', Registration.as_view() , name = 'reg' ),
    path('authorization/', Authorization.as_view() , name = 'aut' ),
    path('logout/', logout_user , name = 'logout' ),

    path('category/<str:slug_category>', Posts_by_category.as_view() , name = 'posts_by_category' ),

    path('blog/<str:slug>', Post_detail.as_view() , name = 'post_detail' ),

]

# Category
# Genre
# Series
# Author
