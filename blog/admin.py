from django.contrib import admin

from .models import News, Razdel, Post, Work, News, File, Instruction, FZayavki, Normativ


class FileAdmin(admin.TabularInline):
    model = File

class InstructionAdmin(admin.TabularInline):
    model = Instruction

class FZayavkiAdmin(admin.TabularInline):
    model = FZayavki

class NormativAdmin(admin.TabularInline):
    model = Normativ


class RazdelAdmin(admin.ModelAdmin):
    list_display = ('sname', 'fname', 'created_on')
    search_fields = ['sname', 'fname', 'description']
    prepopulated_fields = {'slug': ('sname', )}


class WorkAdmin(admin.ModelAdmin):
    list_display = ('sname', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['sname', 'description']
    prepopulated_fields = {'slug': ('sname',)}
    inlines = [
        FileAdmin,
        InstructionAdmin,
        FZayavkiAdmin,
        NormativAdmin
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'desc']
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post, PostAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Razdel, RazdelAdmin)
admin.site.register(News, NewsAdmin)
