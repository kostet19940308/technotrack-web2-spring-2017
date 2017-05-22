from rest_framework import routers
from ugc.views import PostViewSet
from chat.views import ChatViewSet, MessageViewSet
from core.views import UserListViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'users', UserListViewSet)
