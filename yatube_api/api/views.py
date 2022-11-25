from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from posts.models import Group, Post, User
from .serializers import (CommentSerializer, GroupSerializer, PostSerializer,
						  FollowSerializer)
from .permissions import IsAuthorOrReadOnly


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['group']

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
	serializer_class = CommentSerializer
	permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

	def get_queryset(self):
		post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
		return post.comments.all()

	def perform_create(self, serializer):
		post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
		serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
	serializer_class = FollowSerializer
	permission_classes = (permissions.IsAuthenticated,)
	http_method_names = ('get', 'post')

	def get_queryset(self):
		user = get_object_or_404(User, username=self.request.user.username)
		return user.follower

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
