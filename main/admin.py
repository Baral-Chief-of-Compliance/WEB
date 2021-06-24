from django.contrib import admin

# Register your models here.
from . models import Card
from . models import Player

admin.site.register(Card)
admin.site.register(Player)
