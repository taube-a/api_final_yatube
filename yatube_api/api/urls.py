from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')
v1_router.register('follow', FollowViewSet, basename='follow')

jwtpatterns = [path('', include('djoser.urls')),
               path('', include('djoser.urls.jwt')), ]

urlpatterns = [path('v1/', include(v1_router.urls)),
               path('v1/', include(jwtpatterns)), ]
