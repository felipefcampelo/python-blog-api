from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment
from blog.serializers import UserSerializer, PostSerializer, CommentSerializer

class UserSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@testuser.com',
            password='testpassword'
        )

    def test_user_serializer(self):
        serializer = UserSerializer(self.user)
        expected_data = {
            'id': self.user.id,
            'username': 'testuser',
            'email': 'test@testuser.com',
        }
        self.assertEqual(serializer.data, expected_data)


class PostSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Title', content='Test Content', author=self.user)

    def test_post_serializer(self):
        serializer = PostSerializer(self.post)
        expected_data = {
            'id': self.post.id,
            'title': 'Test Title',
            'content': 'Test Content',
            'created_at': self.post.created_at.isoformat().replace('+00:00', 'Z'),
            'updated_at': self.post.updated_at.isoformat().replace('+00:00', 'Z'),
            'author': self.user.id,
        }
        self.assertEqual(serializer.data, expected_data)


class CommentSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Title', content='Test Content', author=self.user)
        self.comment = Comment.objects.create(content='Comment Content', post=self.post, author=self.user)

    def test_comment_serializer(self):
        serializer = CommentSerializer(self.comment)
        expected_data = {
            'id': self.comment.id,
            'content': 'Comment Content',
            'author': self.user.id,
            'post': self.post.id,
            'created_at': self.comment.created_at.isoformat().replace('+00:00', 'Z'),
            'updated_at': self.comment.updated_at.isoformat().replace('+00:00', 'Z'),
        }
        self.assertEqual(serializer.data, expected_data)

