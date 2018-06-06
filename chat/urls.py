from django.contrib.auth.views import logout
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include


urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat_view, name='chats'),
    path('api/messages', views.message_list, name='message-list'),
    path('api/users', views.user_list, name='user-list'),
    path('logout', logout, {'next_page': 'index'}, name='logout'),
    path('register', views.register_view, name='register'),
    path(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    path(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    path(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    path(r'^oauth/', include('social_django.urls', namespace='social')),
]
