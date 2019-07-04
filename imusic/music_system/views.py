from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse

from .models import user, artist, album, music
from .genData import genData


# auth
@login_required
def login_redirect(req):
    """ 这个函数负责重定向，登录之后按照用户的类别重定向到对应的界面 """
    user_group = str(req.user.groups.all()[0].name)
    if user_group == 'artist':
        return HttpResponseRedirect(reverse('music_system:artist_profile'))
    elif user_group == 'user':
        return HttpResponseRedirect(reverse('music_system:user_profile'))


def logged_out(req):
    return render(req, 'registration/logged_out.html')


def check(u):
    return any(u.groups.filter(name=gp).exists() for gp in ['artist', 'user'])


# index, data
def data(req):
    genData()
    return index(req)


def index(req):
    return render(req, 'music_system/index.html', {})


# music
music_attrs = ['musicId', 'name', 'isVip']


def search_music(req):
    dic = {attr: req.GET[attr]
           for attr in music_attrs if attr in req.GET and req.GET[attr]}
    if 'isVip' in dic:
        if dic['isVip'] == '2':
            del dic['isVip']
        else:
            dic['isVip'] = dic['isVip'] == '1'
    context = {}
    musics = music.objects.filter(**dic)
    if not musics:
        context['info'] = 'No music found, show all'
        musics = music.objects.all()
    for m in musics:
        m.artists = m.artist.all()
    context['musics'] = musics
    return render(req, 'music_system/music.html', context)


# album


album_attrs = ['albumId', 'name']


def search_album(req):
    dic = {attr: req.GET[attr]
           for attr in album_attrs if attr in req.GET and req.GET[attr]}
    context = {}
    objs = album.objects.filter(**dic)
    if not objs:
        context['info'] = 'No album found, show all'
        objs = album.objects.all()
    for m in objs:
        m.artists = m.artist.all()
    context['albums'] = objs
    return render(req, 'music_system/album.html', context)


# artist
artist_attrs = ['artistId', 'name']


def search_artist(req):
    dic = {attr: req.GET[attr]
           for attr in artist_attrs if attr in req.GET and req.GET[attr]}
    context = {}
    objs = artist.objects.filter(**dic)
    if not objs:
        context['info'] = 'No music found, show all'
        objs = artist.objects.all()
    for m in objs:
        m.musics = m.music_set.all()
    context['artists'] = objs
    return render(req, 'music_system/artist.html', context)


@login_required
@user_passes_test(check)
def profile(req):
    user_group = str(req.user.groups.all()[0].name)
    if user_group == 'artist':
        return artist_profile(req)
    else:
        return user_profile(req)


@login_required
@user_passes_test(check)
def artist_profile(req):
    context = {}
    name = req.user.username
    u = artist.objects.get(artistId=name)
    if not u:
        context['info'] = 'Internal error, your data may be removed'
    else:
        context['artist'] = u
        # many to many field, search as this
        context['musics'] = music.objects.filter(artist__artistId=name)
        for m in context['musics']:
            m.artists = m.artist.all()
        context['albums'] = album.objects.filter(artist__artistId=name)
        for m in context['albums']:
            m.artists = m.artist.all()
    return render(req, 'music_system/artist_profile.html', context)


@login_required
@user_passes_test(check)
def user_profile(req):
    context = {}
    name = req.user.username
    u = user.objects.get(userId=name)
    if not u:
        context['info'] = 'Internal error, your data may be removed'
    else:
        context['user_profile'] = u
        if u.isVip:
            context['musics'] = music.objects.all()
        else:
            context['musics'] = music.objects.filter(isVip=False)
            context['vipMusics'] = music.objects.filter(isVip=True)
            for m in context['vipMusics']:
                m.artists = m.artist.all()
        for m in context['musics']:
            m.artists = m.artist.all()
    return render(req, 'music_system/user_profile.html', context)


@login_required
@user_passes_test(check)
def add_music(req):
    pass
