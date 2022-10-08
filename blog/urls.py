from . import views
from django.urls import path
from .feeds import LatestNewsFeed 


urlpatterns = [
    path('', views.PostList, name='home'),
    path('feed/', LatestNewsFeed(), name='news_feed'),
    path('<slug:slug>/', views.PostDetailed, name='razdel'),
    path('news/', views.NewsList, name='news_list'),
    path('news/<slug:slug>/', views.NewsDetail, name='news_detailed')
]
