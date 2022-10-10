from re import template
from django.shortcuts import render, get_object_or_404
from .models import Post, Razdel, Work, RecentBlogPosts, Zakupki, News
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



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
    news = RecentBlogPosts.objects.order_by('-date')
    template_name = 'news/news_list.html'
    context = {
        'razdels': razdels,
        }
    default_page = 1
    page = request.GET.get('page',default_page)
    paginator = Paginator(news,10)
    try:
        context['news_list'] = paginator.page(page)
    except PageNotAnInteger:
        context['news_list'] = paginator.page(1)
    except EmptyPage:
        context['news_list'] = paginator.page(paginator.num_pages)
    return render(request, template_name, context)
                                            

def ZakupkiList(request):
    razdels = Razdel.objects.all()
    zakupki = Zakupki.objects.order_by('-date')
    template_name = 'news/zakupki_list.html'
    context = {
        'razdels': razdels,
        }
    default_page = 1
    page = request.GET.get('page',default_page)
    paginator = Paginator(zakupki,10)
    try:
        context['zakupki_list'] = paginator.page(page)
    except PageNotAnInteger:
        context['zakupki_list'] = paginator.page(1)
    except EmptyPage:
        context['zakupki_list'] = paginator.page(paginator.num_pages)
    return render(request, template_name, context)