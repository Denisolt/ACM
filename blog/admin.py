from django.contrib import admin
from .models import Event, Competition
from .models import Post, User

# Register your models here.
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Competition)
