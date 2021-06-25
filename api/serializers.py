from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class ProfSerializer(serializers.ModelSerializer):
    prof_rating = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()
    count = 0

    def get_prof_rating(self, instance):
        ratings = Ratings.objects.filter(prof_id=instance)
        self.count:int = ratings.count()
        if(self.count == 0):
            return 0
        k = 0;
        for r in ratings:
            k += r.rating
        return k // self.count
    
    def get_count_rating(self, instance):
        return self.count

    class Meta:
        model = Professor
        fields = ('id', 'name', 'dept', 'designation', 'email', 'portfolio_url', 'prof_rating', 'count_rating')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'karma')


class CommentSerializer(serializers.ModelSerializer):
    comment_votes = serializers.SerializerMethodField()

    def get_comment_votes(self, instance):
        votes = Upvotes.objects.filter(comment_id=instance)
        k = 0
        for v in votes:
            k += v.value
        return votes

    class Meta:
        model = Comment
        fields = ('id', 'prof', 'stud', 'content', 'date_added', 'comment_votes')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'
