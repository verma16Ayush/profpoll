from rest_framework import serializers
from .models import *


class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'karma']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
