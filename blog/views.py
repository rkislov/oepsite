from re import template
from django.shortcuts import render, get_object_or_404
from .models import Post, Razdel, Work, RecentBlogPosts, Zakupki, News



def PostList(request):
    razdels = Razdel.objects.prefetch_related('razdel_work')
    posts = Post.objects.filter(status=1).order_by('-created_on')
    works = Work.objects.filter(status=1)
    feed = RecentBlogPosts.objects.all()[:3]
    zakupki = Zakupki.objects.order_by('-date').all()[:3]
    news = News.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'index.html'
    return render(request, template_name, {'posts': posts,
                                           'razdels': razdels,
                                           'works': works,
                                           'feed': feed,
                                           'zakupki': zakupki,
                                           'news': news
                                            })


def PostDetailed(request, slug):
    razdels = Razdel.objects.all()
    post = get_object_or_404(Post, slug=slug)
    template_name = 'post_detailed.html'
    return render(request, template_name, {'post': post,
                                           'razdels': razdels,
                                           })


def NewsList(request):
    razdels = Razdel.objects.all()
    news = News.objects.filter(status=1).order_by('-created_on')
    template_name = 'news/news_list.html'
    return render(request, template_name, {'news': news,
                                            'razdels': razdels,})
                                            

def NewsDetail(request, slug):
    razdels = Razdel.objects.all()
    news = get_object_or_404(News, slug=slug)
    template_name = 'news_detailed.html'
    return render(request, template_name, {'news': news,
                                           'razdels': razdels,
                                           })