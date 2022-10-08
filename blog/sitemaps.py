from django.contrib.sitemaps import Sitemap
from .models import Work, Post, News, Razdel

class RazdelSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Razdel.objects.all()

    def lastmod(self, obj):
        return obj.created_on