from django.contrib import admin
from django.urls import path, include
import movie.views as view

urlpatterns = [
    path('index/', view.index, name='index'),
    path('rank/', view.rank, name='rank'),
    path('near-cgv/', view.nearCGV, name='nearCGV'),
]