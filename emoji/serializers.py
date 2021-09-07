from rest_framework import serializers
from .models import emoji_name,emoji_sym

class sym_serial (serializers.HyperlinkedModelSerializer):

    class Meta:
        model = emoji_sym
        fields = ['id','symbol']

class name_serial (serializers.ModelSerializer):
    emoji_names = sym_serial(many=True)
    
    class Meta:
        model = emoji_name
        fields = ['id','user','ename','emoji_names']
