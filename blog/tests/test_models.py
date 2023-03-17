from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

""" User entity tests """
class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@testuser.com',
        )

    def test_user_creation(self):
        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@testuser.com')

    def test_user_update(self):
        self.user.username = 'testuser123'
        self.user.email = 'test123@testuser123.com'
        self.user.save()

        updated_user = User.objects.get(pk=self.user.pk)

        self.assertEqual(updated_user.username, 'testuser123')
        self.assertEqual(updated_user.email, 'test123@testuser123.com')
    
    def test_user_delete(self):
        self.assertEqual(User.objects.filter(pk=self.user.pk).count(), 1)
        self.user.delete()
        self.assertEqual(User.objects.filter(pk=self.user.pk).count(), 0)


""" Post entity tests """
class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@testuser.com', 
            password='testpassword'
        )
        self.post = Post.objects.create(
            title='Test title', 
            content='Test content', 
            author=self.user
        )
    
    def test_post_creation(self):
        post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(post.title, 'Test title')
        self.assertEqual(post.content, 'Test content')
        self.assertEqual(post.author, self.user)

    def test_post_update(self):
        self.post.title = 'Updated Test Post'
        self.post.content = 'This is an updated test post'
        self.post.save()

        updated_post = Post.objects.get(pk=self.post.pk)

        self.assertEqual(updated_post.title, 'Updated Test Post')
        self.assertEqual(updated_post.content, 'This is an updated test post')
    
    def test_post_delete(self):
        self.assertEqual(Post.objects.filter(pk=self.post.pk).count(), 1)
        self.post.delete()
        self.assertEqual(Post.objects.filter(pk=self.post.pk).count(), 0)