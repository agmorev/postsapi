from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('signup/', views.UserSignupView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    path('users/<int:pk>/activity/', views.UserActivityView.as_view()),    
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('posts/create/', views.PostCreateView.as_view()),
    path('posts/update/<int:pk>/', views.PostUpdateView.as_view()),
    path('posts/delete/<int:pk>/', views.PostDeleteView.as_view()),
    path('posts/likes/', views.LikeListView.as_view()),
    path('posts/<int:pk>/likes/', views.PostLikeListView.as_view()),
    path('posts/likes/analytics/', views.LikeAnalyticsView.as_view()),
    path('posts/dislikes/', views.DislikeListView.as_view()),
    path('posts/<int:pk>/dislikes/', views.PostDislikeListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)