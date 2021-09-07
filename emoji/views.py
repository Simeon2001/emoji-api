from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import emoji_name,emoji_sym
from .serializers import name_serial,sym_serial
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# link view
@api_view()
def emoji_search (request,mood):
    permission_classes = (AllowAny,)
    find = emoji_name.objects.get(ename=mood)
    symbol = emoji_sym.objects.filter(name=find)
    serializer_class = sym_serial(symbol,many=True)
    return Response(serializer_class.data)
