import feedparser

import pytz
from datetime import datetime

from django.core.management.base import BaseCommand

from blog.models import Zakupki

class Command(BaseCommand):
   # args = ''
    help = 'Gets N recent blog posts. Better than parsing the list every page load.'
    
    def handle(self, *args, **options):
        num_blog_posts = 100
        tz =  pytz.timezone('Asia/Yekaterinburg')
        feed = feedparser.parse('https://zakupki.gov.ru/tinyurl/dd5f725ab013f8e834007c3265b819abcafe999ec2f2add484540dbfafffba54')

        for blog in Zakupki.objects.all():
            blog.delete()

        loop_max = num_blog_posts if len(feed['entries']) > num_blog_posts else len(feed['entries'])

        for i in range(0, loop_max):
            if feed['entries'][i]:
                blog_post = Zakupki()
                blog_post.title = feed['entries'][i].summary.split('<br />')[7].replace('&nbsp;','').replace('&#039;','').replace('<strong>Наименование объекта закупки: </strong>', '').replace('&laquo;','"').replace('&raquo;','"').replace('&quot;','"')
                blog_post.link = feed['entries'][i].link
                blog_post.price = feed['entries'][i].summary.split('<br />')[10].replace('&nbsp;','').replace('&#039;','').replace('<strong>Начальная цена контракта: </strong>','').replace('<strong> Валюта: </strong>Российский рубль','')
                blog_post.type = feed['entries'][i].title
                blog_post.date = tz.localize(datetime.strptime(feed['entries'][i].summary.split('<br />')[11].replace('&nbsp;','').replace('&#039;','').replace('<strong>Размещено: </strong>', ''), '%d.%m.%Y'))
                blog_post.save()