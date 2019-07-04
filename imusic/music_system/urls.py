from django.urls import path, include
from . import views

app_name = 'music_system'

urlpatterns = [

    # index
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('data', views.data, name='data'),


    # authentication
    path('redirect', views.login_redirect, name='redirect'),
    path('logout', views.logged_out, name='logout'),


    # general info
    path('music.html', views.search_music, name='search_music'),
    path('artist.html', views.search_artist, name='search_artist'),
    path('album.html', views.search_album, name='search_album'),



    # user logged in
    path('user_profile', views.user_profile, name='user_profile'),
    path('artist_profile', views.artist_profile, name='artist_profile'),
    path('profile', views.profile, name='profile'),
]
'''
# authentication
# includeing url patterns: accounts/{login,logout,password_chage,password_reset,...
path('accounts/', include('django.contrib.auth.urls')),
'''
