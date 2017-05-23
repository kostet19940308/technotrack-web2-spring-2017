from rest_framework import routers
from ugc.views import PostViewSet
from chat.views import ChatViewSet, MessageViewSet, ChatMembersViewSet
from core.views import UserListViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'chats/(?P<chat_id>[^/.]+)/messages', MessageViewSet)
router.register(r'users', UserListViewSet)
router.register(r'chats/(?P<chat_id>[^/.]+)/members', ChatMembersViewSet)
