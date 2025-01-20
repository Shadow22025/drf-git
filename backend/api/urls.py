from django.urls import path, include
from . import views

app_name = "api"

urlpatterns = [
    path("", views.ArticleList.as_view(), name = "list"),
    path("<int:pk>", views.ArticleDetail.as_view(), name = "detail"),
    path("list_api/", views.ArticleList_list_api_view.as_view(), name = "list_api"),
    path("list_api/<int:pk>", views.ArticleDetail_list_api_view.as_view(), name = "detail_api"),
    path("user/", views.UserList.as_view(), name = "user-list"),
    path("user/<int:pk>", views.UserDetail.as_view(), name = "user-detail"),
]

