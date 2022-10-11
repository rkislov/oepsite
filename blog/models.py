import uuid
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Razdel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    icon = models.CharField(max_length=2000, blank=True, null=True)
    sname = models.CharField(max_length=50, unique=True)
    fname = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = RichTextUploadingField(blank=True, null=True)
    update_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name= "Раздел"
        verbose_name_plural= "Разделы"

    def get_absolute_url(self):
      return reverse('razdel', kwargs={'slug': self.slug })

    def __str__(self):
        return self.sname

class Work(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sname = models.CharField(max_length=50, unique=True)
    fname = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='works'
        )
    update_on = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(blank=True, null=True)
    razdel = models.ForeignKey(
        Razdel,
        on_delete=models.CASCADE,
        related_name="razdel_work",
        default=0
    )
    parent_id = models.UUIDField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


    class Meta:
        verbose_name= "Работа"
        verbose_name_plural= "Работы"

    def __str__(self):
        return self.sname


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
        )
    update_on = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(blank=True, null=True)
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name="work_posts",
        default=0,
        null=True
    )
    parent_id = models.UUIDField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        #ordering = ['-created_on']
        verbose_name= "Стать"
        verbose_name_plural= "Статьи"
    
    def __str__(self):
        return self.title


class RecentBlogPosts(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2048)
    desc = models.TextField(null=True, blank=True)
    date = models.DateTimeField()


class Zakupki(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=2048)
    price = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    date = models.DateTimeField()


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    desc = RichTextUploadingField(blank=True, null=True)
    parent_id = models.UUIDField(blank=True, null=True)
    update_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    tech = models.BooleanField(default=False, verbose_name="Технические работы")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news'
        )
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name="work_news",
        blank=True,
        null=True
    )
    class Meta:
            #ordering = ['-created_on']
            verbose_name= "Новость"
            verbose_name_plural= "Новости"


    def get_absolute_url(self):
      return reverse('news_detailed', kwargs={'slug': self.slug })
        
    def __str__(self):
        return self.title


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='files'
        )
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/')
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name="work_files",
        default=0,
        null=True
    )

    def __str__(self):
        return self.title
    
    def path(self):
        return self.url
