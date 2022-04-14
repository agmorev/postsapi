
from rest_framework import generics
from . import serializers
from users.models import User
from posts.models import Post, Like, Dislike
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.db.models import Count



class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSignupSerializer
    permission_classes = [permissions.AllowAny]

class UserActivityView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserActivitySerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

class PostCreateView(generics.CreateAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    filter_fields = ['user', 'created']

class PostLikeListView(generics.ListAPIView):
    serializer_class = serializers.LikeSerializer
    
    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = Like.objects.filter(post_id=post_id)
        return queryset
    
class DislikeListView(generics.ListAPIView):
    queryset = Dislike.objects.all()
    serializer_class = serializers.DislikeSerializer

class PostDislikeListView(generics.ListAPIView):
    serializer_class = serializers.DislikeSerializer
    
    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = Dislike.objects.filter(post_id=post_id)
        return queryset

class LikeAnalyticsView(generics.ListAPIView):
    serializer_class = serializers.LikeAnalyticsSerializer
    queryset = Like.objects.all()
    
    def get_queryset(self):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        if date_from is not None and date_to is not None:
            queryset = self.queryset.filter(created__gte=date_from, created__lte=date_to).values('created').annotate(count=Count('id'))
            print(queryset)
        return queryset
