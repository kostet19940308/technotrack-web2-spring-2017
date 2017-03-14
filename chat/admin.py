from django.contrib import admin

from chat.models import Chat, Message

class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')

admin.site.register(Chat, ChatAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'chat', 'title')

admin.site.register(Message, MessageAdmin)