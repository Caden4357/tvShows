from django.urls import path,include
from  . import views
urlpatterns = [
    path('',views.index),
    path('directors',views.directors),
    path('directors/<int:id>',views.show_director),
    path('directors/create',views.create_director),
    path('directors/<int:id>/destroy',views.destroy_director),

    path('movies',views.movies),
    path('movies/create',views.create_movie),
    path('movies/<int:id>',views.show_movie),
    path('movies/<int:id>/edit',views.edit_movie),
    path('movies/<int:id>/update',views.update_movie),
    path('movies/<int:id>/destroy',views.destroy_movie),

]


