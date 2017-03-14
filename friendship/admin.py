from django.contrib import admin

from friendship.models import FriendShip, Friends

class FriendShipAdmin(admin.ModelAdmin):
    pass

admin.site.register(FriendShip, FriendShipAdmin)


class FriendAdmin(admin.ModelAdmin):
    pass

admin.site.register(Friends, FriendAdmin)