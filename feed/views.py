from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Feed
from .serializers import FeedSerializer
from api.pagination import ResultsSetPagination
from api.permissions import ReadOnly, IsContentOfFriends


class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    #pagination_class = ResultsSetPagination
    permission_classes = (permissions.IsAuthenticated, ReadOnly, IsContentOfFriends)

    def get_queryset(self):
        queryset = super(FeedViewSet, self).get_queryset()
        if 'author' in self.request.query_params:
            return queryset.filter(author=self.request.query_params['author'])
        return queryset.filter(author=self.request.user)