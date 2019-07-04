from django.contrib import admin

from .models import *

admin.site.register(user)
admin.site.register(artist)
admin.site.register(music)
admin.site.register(album)
