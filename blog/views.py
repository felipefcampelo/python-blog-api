from django.contrib.auth.models import User
from rest_framework import generics, response, status
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer


""" Users """
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Get data coming from request, stores the password and remove it from data
        data = request.data
        password = data.get('password')
        data.pop('password')
        
        # Serialize the information without password
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        # Apply the validated data to the user, create the hashed password, and save
        user = User(**serializer.validated_data)
        user.set_password(password)
        user.save()

        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # return the list of users after deletion
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
    
class UserDeleteAll(generics.GenericAPIView):
    queryset = User.objects.all()

    def delete(self, request, *args, **kwargs):
        self.queryset.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


""" Posts """
class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # return the list of posts after deletion
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
    
class PostDeleteAll(generics.GenericAPIView):
    queryset = Post.objects.all()

    def delete(self, request, *args, **kwargs):
        self.queryset.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


""" Comments """
class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # return the list of users after deletion
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
    
class CommentDeleteAll(generics.GenericAPIView):
    queryset = Post.objects.all()

    def delete(self, request, *args, **kwargs):
        self.queryset.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)