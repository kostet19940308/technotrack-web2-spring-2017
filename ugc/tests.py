from django.test import TestCase
from feed.models import Feed
from .models import Post
from django.contrib.auth import get_user_model

# Create your tests here.
class PostFeedableTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username="test_user")

    def test_new_post_add_feed(self):
        feed_count_before_post = Feed.objects.count()
        self.assertEqual(feed_count_before_post, 0)

        post = Post.objects.create(author=self.user)
        feed_count_after_post = Feed.objects.count()
        self.assertEqual(feed_count_after_post, 1)

    def test_new_post_add_feed_old_not(self):

        post = Post.objects.create(author=self.user)
        feed_count_before_post = Feed.objects.count()
        self.assertEqual(feed_count_before_post, 1)

        post.text = "blaaaaaaaaaaaaaaaaaaaaaaa"
        post.save()
        feed_count_after_post = Feed.objects.count()
        self.assertEqual(feed_count_after_post, 1)