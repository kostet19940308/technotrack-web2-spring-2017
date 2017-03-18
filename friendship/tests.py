from django.db.models import Q
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import FriendShip, Friends
from feed.models import Feed


class BaseFriendTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="user")
        self.friend = get_user_model().objects.create(username="friend")

class CreateFriendsTestCase(BaseFriendTestCase, TestCase):

    def testOnCreateFriendShipNotFrineds(self):
        self.assertEqual(Friends.objects.count(), 0)
        self.assertEqual(FriendShip.objects.count(), 0)

        friendShip = FriendShip.objects.create(author=self.user, recipient=self.friend, approved=False)
        self.assertEqual(FriendShip.objects.count(), 1)
        self.assertEqual(Friends.objects.count(), 0)

    def testOnFrinedShipNotBecomeApproved(self):
        self.assertEqual(Friends.objects.count(), 0)
        self.assertEqual(FriendShip.objects.count(), 0)

        friendShip = FriendShip.objects.create(author=self.user, recipient=self.friend, approved=False)
        friendShip.approved = False
        friendShip.save()
        self.assertEqual(FriendShip.objects.count(), 1)
        self.assertEqual(Friends.objects.count(), 0)

    def testOnFriendShipBecomeApproved(self):
        self.assertEqual(Friends.objects.count(), 0)
        self.assertEqual(FriendShip.objects.count(), 0)

        friendShip = FriendShip.objects.create(author=self.user, recipient=self.friend, approved=False)
        friendShip.approved = True
        friendShip.save()
        self.assertEqual(FriendShip.objects.count(), 1)
        self.assertEqual(Friends.objects.count(), 2)

        self.assertEqual(Friends.objects.filter(Q(user=self.user) and Q(friend=self.friend)).count(), 1,
                         msg="Not created Frieds node from author to recipient")
        self.assertEqual(Friends.objects.filter(Q(user=self.friend) and Q(friend=self.user)).count(), 1,
                         msg="Not created Frieds node from recipient to author")


class FriendsFeedTestCase(BaseFriendTestCase, TestCase):
    def testOnFriendCreateFeedCreate(self):
        self.assertEqual(Friends.objects.count(), 0)
        self.assertEqual(Feed.objects.count(), 0)

        friendShip = FriendShip.objects.create(author=self.user, recipient=self.friend, approved=False)
        self.assertEqual(Friends.objects.count(), 0)
        self.assertEqual(Friends.objects.count(), 0)

        friendShip.approved =True
        friendShip.save()
        self.assertEqual(Friends.objects.count(), 2)
        self.assertEqual(Feed.objects.count(), 2)

        feed1 = Feed.objects.all()[0]
        feed2 = Feed.objects.all()[1]
        self.assertFalse(feed1.author.username == feed2.author.username,
                         msg = "Authors of feeds are equal" )
        self.assertTrue((feed1.author.username == 'user') or (feed1.author.username == 'friend'),
                        msg="Wrong author for feed(pk=1)")
        self.assertTrue((feed2.author.username == 'user') or (feed2.author.username == 'friend'),
                        msg="Wrong author for feed(pk=2)")

        self.assertEqual(feed1.text, 'user becomes friend of friend',
                         msg="Wrong text feed(pk=1)" + feed1.text)
        self.assertEqual(feed2.text, 'friend becomes friend of user',
                         msg="Wrong text feed(pk=2)")