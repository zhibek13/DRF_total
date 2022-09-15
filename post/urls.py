from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('tweet', views.TweetViewSet, basename='tweet')
# router.register('comment', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('tweet/<int:tweet_id>/comments/', views.CommentListCreateAPIView.as_view()),
    path('tweet/<int:tweet_id>/comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('tweet/<int:tweet_id>/<str:status_slug>/', views.PostTweetLike.as_view()),
    path('tweet/<int:tweet_id>/comments/<int:comment_id>/<str:status_slug>/', views.PostCommentLike.as_view()),
    # path('tweet/<int:tweet_id>/dislike/', views.PostTweetDislike.as_view()),
    # path('tweet/<int:comment_id>/like/', views.PostCommentLike.as_view()),
    # path('tweet/<int:comment_id>/dislike/', views.PostCommentDislike.as_view()),
]