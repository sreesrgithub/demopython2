from django.urls import path
from . import views

app_name = 'movieapp'

urlpatterns = [

    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('edit/<int:movie_id>/', views.edit, name='edit'),
    path('delete/<int:movie_id>/', views.delete, name='delete'),
    path('add_movie', views.add_movie, name='add_movie'),

]
