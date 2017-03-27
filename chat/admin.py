from django.contrib import admin
from django.contrib.admin import StackedInline
from chat.models import Chat, Message

class MessageInLine(StackedInline):
    model = Message
    ordering = ("-created_at", )
    extra = 1

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    inlines = [MessageInLine,]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'chat', 'title')
