from django.shortcuts import render
from blog.models import Article
from .serialisers import ArticleSerialiser, UserSerialiser
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveDestroyAPIView
from rest_framework.generics import UpdateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .premissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
# Create your views here.


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    # lookup_field = "slug"
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class ArticleList_list_api_view(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser


class ArticleDetail_list_api_view(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser



class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (IsSuperUserOrStaffReadOnly,)