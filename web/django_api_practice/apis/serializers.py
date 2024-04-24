from rest_framework import serializers
from .models import Apis

class ApiListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apis
        fields = ('title',)

class ApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apis
        fields = ('title','content')