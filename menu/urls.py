from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('chapter/', views.chapter, name='chapter_menu'),
    path("verse/", views.verse, name="verse_menu")
]
