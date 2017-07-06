from django.shortcuts import render
from .models import Award
from rest_framework import serializers, viewsets, permissions, fields
from .serializers import AwardSerializer
from api.permissions import ReadOnly, IsContentOfFriends
from django.db.models import Q

class AwardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    permission_classes = (permissions.IsAuthenticated, ReadOnly, IsContentOfFriends)

    def get_queryset(self):
        q = self.queryset
        if 'author' in self.request.query_params:
            q = q.filter(author=self.request.query_params['author'])
        else:
            q = q.filter(author=self.request.user)
        return q
