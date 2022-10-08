from django.contrib.syndication.views import Feed  
from django.template.defaultfilters import truncatewords  
from .models import News  
  
  
class LatestNewsFeed(Feed):  
    title = 'ГБУ СО "ОЭП"'  
    link = '/news/'  
    description = 'Последние новости'  
    def items(self):  
        return News.objects.all()[:5]  
      
    def item_title(self, item):  
        return item.title  
      
    def item_description(self, item):  
        return truncatewords(item.desc, 30)