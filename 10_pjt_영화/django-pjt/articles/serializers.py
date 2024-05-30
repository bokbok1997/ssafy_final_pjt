from rest_framework import serializers
from .models import Review, Movie, Comment
from django.contrib.auth import get_user_model


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'movie', 'user')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user',)
        # movie는 왜 read only가 아닌가? << movie는 post 할 때 같이 넣어줘야 할 듯?

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)
        # 여기도 마찬가지로 post 할 때 review pk를 같이 넣어줘야 할 듯?

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = get_user_model()
        fields = ('username',)