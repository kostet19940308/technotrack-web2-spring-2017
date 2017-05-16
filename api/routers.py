from rest_framework import routers
from ugc.views import PostViewSet
from chat.views import ChatViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)

