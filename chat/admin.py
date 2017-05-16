from django.contrib import admin
from django.contrib.admin import StackedInline, TabularInline
from chat.models import Chat, Message, ChatMembership

class MessageInLine(TabularInline):
    model = Message
    ordering = ("-created_at", )
    extra = 1
    fields = ('author', 'title', 'text')

class ChatMembershipInLine(TabularInline):
    model = ChatMembership
    ordering = ("-created_at", )
    extra = 1
    fields = ('user', 'inviter')

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    inlines = [MessageInLine, ChatMembershipInLine,]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'chat', 'title')


@admin.register(ChatMembership)
class ChatMembershipAdmin(admin.ModelAdmin):
    pass