from django.contrib import admin
from .models import emoji_name,emoji_sym

# Register your models here.

admin.site.register(emoji_name)
admin.site.register(emoji_sym)