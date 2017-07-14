from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework import permissions, mixins
from rest_framework.response import Response

from .serializers import UserSerializer, UserAuthorSerializer, UserFriendSerializer
from .models import User
from .permissions import IsOwnerOrReadOnly
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserListViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    #serializer_class = self.get_user_serializer(self.action)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_serializer(self, *args, **kwargs):
        # user = self.obj
        # request_user = self.request.user
        serializer_class = None
        if self.action == 'list':
            serializer_class = UserAuthorSerializer
        elif self.action == 'retrieve':
            serializer_class = UserFriendSerializer
        else:
            serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        queryset = super(UserListViewSet, self).get_queryset()
        #status = self.request.query_params.get('status')
        if 'myself' in self.request.query_params:
            return queryset.filter(id=self.request.user.id)
        return queryset


def home(request):
    return render(request, template_name='index.html')

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email',  'first_name', 'last_name']

    def clean_username(self):
        try:
            User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("The username already exists. Please try another one.")

    def clean_email(self):
        try:
            User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError("This e-mail is already used.")

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two password fields did not match.")
        return self.cleaned_data


class RegisterView(CreateView):
    model = User
    template_name = 'login/registration.html'
    form_class = RegistrationForm
    success_url = 'core:login'

    def get_success_url(self):
        return reverse(self.success_url)