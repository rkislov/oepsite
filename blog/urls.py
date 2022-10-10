from . import views
from django.urls import path
from .feeds import LatestNewsFeed 


urlpatterns = [
    path('', views.PostList, name='home'),
    path('feed/', LatestNewsFeed(), name='news_feed'),
    path('razdel/<slug:slug>/', views.PostDetailed, name='razdel'),
    path('news/', views.NewsList, name='news_list'),
    path('zakupki/', views.ZakupkiList, name='zakupki_list')
]
