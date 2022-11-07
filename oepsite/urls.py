from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import RazdelSitemap


sitemaps = {
    'razdels': RazdelSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^webpush/', include('webpush.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
