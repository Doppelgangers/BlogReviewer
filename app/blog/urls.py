from django.urls import path , include
from .views import *

urlpatterns = [
    path('', index , name = 'home' ),
    path('registration/', Registration.as_view() , name = 'reg' ),
    path('authorization/', Authorization.as_view() , name = 'aut' ),
    path('logout/', logout_user , name = 'logout' ),
]