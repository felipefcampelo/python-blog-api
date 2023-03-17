from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta: # What are the Meta Classes? Can we create a class inside a class in Python?
        model = Comment
        fields = ['id', 'content', 'author', 'post', 'created_at', 'updated_at']