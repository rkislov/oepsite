from django.contrib import admin
from .models import Profile, Message



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')
    

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)