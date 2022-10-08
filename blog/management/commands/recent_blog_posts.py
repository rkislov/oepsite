import feedparser

from time import mktime
from datetime import datetime
import pytz
from django.core.management.base import BaseCommand

from blog.models import RecentBlogPosts

class Command(BaseCommand):
   # args = ''
    help = 'Gets N recent blog posts. Better than parsing the list every page load.'
    
    def handle(self, *args, **options):
        num_blog_posts = 100
        tz =  pytz.timezone('Asia/Yekaterinburg')
        feed = feedparser.parse('https://digital.midural.ru/rss')

        for blog in RecentBlogPosts.objects.all():
            blog.delete()

        loop_max = num_blog_posts if len(feed['entries']) > num_blog_posts else len(feed['entries'])

        for i in range(0, loop_max):
            if feed['entries'][i]:
                blog_post = RecentBlogPosts()
                blog_post.title = feed['entries'][i].title
                blog_post.link = feed['entries'][i].link
                blog_post.desc = feed['entries'][i].description
                blog_post.date = tz.localize(datetime.fromtimestamp(mktime(feed['entries'][i].published_parsed)))
                blog_post.save()