from django.contrib import admin
from django.urls import path, include
import api.views as view

urlpatterns = [
    path('test/', view.test, name='test'),
    path('movie-rank/', view.movieRank, name='movieRank'),
]