from . import views
from django.urls import path
from .feeds import LatestNewsFeed 


urlpatterns = [
    path('', views.PostList, name='home'),
    path('feed/', LatestNewsFeed(), name='news_feed'),
    path('razdel/<slug:slug>/', views.WorkList, name='razdel'),
    path('razdel/work/<slug:slug>/', views.WorkDetailed, name='work'),
    path('news/', views.NewsList, name='news_list'),
    path('news/<slug:slug>', views.PostDetailed, name='news_detailed'),
    path('zakupki/', views.ZakupkiList, name='zakupki_list')
]
