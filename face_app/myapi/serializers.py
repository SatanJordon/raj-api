from rest_framework import serializers

from .models import User_Face


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Face
        fields = ('id', 'name', 'gender', 'age', 'password', 'mobile')
