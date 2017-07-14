
from django.conf.urls import url
from .views import RegisterView
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from application.settings import LOGIN_URL


urlpatterns = [
    url(r'^logout/$', login_required(logout, login_url=LOGIN_URL), {'next_page': '/'}, name='logout'),
    url(r'^login/$', login, {'template_name': 'login/login.html',
                             'redirect_authenticated_user': True,
                             'extra_context': {
                                'authform': AuthenticationForm()
                             }}, name='login'),
    url(r'^registration/$', RegisterView.as_view(), name='registration'),
]