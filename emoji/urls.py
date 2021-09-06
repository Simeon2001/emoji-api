from django.urls import path
from . import views

urlpatterns = [
    path ('s/<str:mood>', views.emoji_search, name = 'emoji' ),

]